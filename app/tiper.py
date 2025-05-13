import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def string_to_weather_code(weather_condition):
    weather_conditions = ["Clear", "Partly Cloudy ", "Rain", "Thunderstorms", "Windy", "Hot", "Cloudy ", "Sunny", "Patchy rain nearby", "Moderate rain"]

    from sklearn.preprocessing import LabelEncoder

    weather_encoder = LabelEncoder()
    weather_encoder.fit(weather_conditions)

    if weather_condition not in weather_conditions:
        raise ValueError(f"'{weather_condition}' is not a valid weather condition. Choose from: {weather_conditions}")

    code = weather_encoder.transform([weather_condition])[0]
    return code


def aviation_tip(temperature, humidity, wind_speed_knots, visibility, rainfall, weather_condition):
    clf_path = os.path.join(BASE_DIR, "aviation_tip_model.pkl")
    encoder_path = os.path.join(BASE_DIR, "tip_encoder.pkl")

    clf = joblib.load(clf_path)
    tip_encoder = joblib.load(encoder_path)

    weather_code = string_to_weather_code(weather_condition)

    input_data = pd.DataFrame([{
        "Temperature_C": temperature,
        "Humidity_%": humidity,
        "Wind_Speed_knots": wind_speed_knots,
        "Visibility_km": visibility,
        "Rainfall_mm": rainfall,
        "Weather_Code": weather_code
    }])

    predicted_label = clf.predict(input_data)[0]
    predicted_tip = tip_encoder.inverse_transform([predicted_label])[0]

    return predicted_tip


def mining_tip(temperature, humidity, wind_speed_kph, rainfall, weather_condition):
    clf_path = os.path.join(BASE_DIR, "mining_tip_model.pkl")
    encoder_path = os.path.join(BASE_DIR, "mining_tip_encoder.pkl")

    clf = joblib.load(clf_path)
    tip_encoder = joblib.load(encoder_path)

    weather_code = string_to_weather_code(weather_condition)

    input_data = pd.DataFrame([{
        "Temperature_C": temperature,
        "Humidity_%": humidity,
        "Wind_Speed_kph": wind_speed_kph,
        "Rainfall_mm": rainfall,
        "Weather_Code": weather_code
    }])
    predicted_label = clf.predict(input_data)[0]
    predicted_tip = tip_encoder.inverse_transform([predicted_label])[0]

    return predicted_tip


def transport_tip(temperature, humidity, wind_speed_kph, rainfall, weather_condition):
    clf_path = os.path.join(BASE_DIR, "transport_tip_model.pkl")
    encoder_path = os.path.join(BASE_DIR, "transport_tip_encoder.pkl")

    clf = joblib.load(clf_path)
    tip_encoder = joblib.load(encoder_path)

    weather_code = string_to_weather_code(weather_condition)

    input_data = pd.DataFrame([{
        "Temperature_C": temperature,
        "Humidity_%": humidity,
        "Wind_Speed_kph": wind_speed_kph,
        "Rainfall_mm": rainfall,
        "Weather_Code": weather_code
    }])

    predicted_label = clf.predict(input_data)[0]
    predicted_tip = tip_encoder.inverse_transform([predicted_label])[0]

    return predicted_tip
