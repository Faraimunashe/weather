from flask import Blueprint, render_template, request
from flask_login import login_required
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
analytic_bp = Blueprint('analytic', __name__)

csv_paths = {
    "agriculture": os.path.join(BASE_DIR, "agriculture.csv"),
    "aviation": os.path.join(BASE_DIR, "aviation.csv"),
    "mining": os.path.join(BASE_DIR, "mining.csv"),
    "transport": os.path.join(BASE_DIR, "transport.csv")
}

def detect_label_column(df):
    for col in df.columns[::-1]:
        if 'tip' in col.lower():
            return col
    return df.columns[-1]

@analytic_bp.route('/analytics', methods=['GET'])
@login_required
def analytics():
    selected = request.args.get("dataset", "agriculture")
    path = csv_paths.get(selected)
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Month"] = df["Date"].dt.strftime("%B")

    month_order = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)

    label_col = detect_label_column(df)
    label_encoder = LabelEncoder()
    df[label_col] = label_encoder.fit_transform(df[label_col].astype(str))

    X = df.select_dtypes(include="number").drop(columns=[label_col], errors="ignore")
    y = df[label_col]

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
    model = RandomForestClassifier(n_estimators=100).fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    conf = confusion_matrix(y_test, model.predict(X_test)).tolist()
    importances = model.feature_importances_

    daily_agg = df.groupby("Date")[["Temperature_C", "Rainfall_mm"]].mean().dropna().reset_index()
    daily_line_data = {
        "labels": daily_agg["Date"].dt.strftime("%Y-%m-%d").tolist(),
        "temperature": daily_agg["Temperature_C"].round(2).tolist(),
        "rainfall": daily_agg["Rainfall_mm"].round(2).tolist()
    }

    # Boxplot Data
    boxplot_data = df.groupby("Month", observed=True)["Temperature_C"].apply(list).dropna().to_dict()


    # Correlation Heatmap
    corr = df.select_dtypes(include="number").corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Correlation Matrix")
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    corr_image_base64 = base64.b64encode(buffer.read()).decode("utf-8")

    chart_data = {
        "feature": {"labels": list(X.columns), "values": importances.tolist()},
        "daily": daily_line_data,
        "boxplot": boxplot_data
    }

    return render_template("analytics.html",
                           datasets=csv_paths.keys(),
                           selected=selected,
                           accuracy=round(acc*100, 2),
                           head=df.head().to_dict(orient="records"),
                           conf_matrix=conf,
                           correlation_image=corr_image_base64,
                           chart_data=chart_data)
