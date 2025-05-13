from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from . import db
from app.models import User
from datetime import datetime, date
from .weatherapi import get_weather_forecast
from .tiper import *

forecast_bp = Blueprint('forecast', __name__)

@forecast_bp.route('/forecast', methods=['GET', 'POST'])
@login_required
def forecast():
    
    return render_template('forecast.html')



@forecast_bp.route('/agriculture', methods=["GET", "POST"])
@login_required
def agriculture():
    forecast_data = []
    tips = []
    city = ""
    day=None
    first_day = [] 
    tip=""
    days = ""

    if request.method == 'POST':
        city = request.form.get('city')
        days = request.form.get('days', type=int)

        try:
            response = get_weather_forecast(city, days)
            if response.status_code == 200:
                data = response.json()
                for day in data["forecast"]["forecastday"]:
                    entry = {
                        "date": day["date"],
                        "temp": round(day["day"]["avgtemp_c"], 1),
                        "rainfall": round(day["day"]["totalprecip_mm"], 1),
                        "humidity": round(day["day"]["avghumidity"], 1),
                        "condition": day["day"]["condition"]["text"],
                        "wind_kph": day["day"]["maxwind_kph"],
                        "vis_km": day["day"]["avgvis_km"],
                        "chance_of_rain": day["day"]["daily_chance_of_rain"],
                    }
                    forecast_data.append(entry)
                first_day = forecast_data[0]
                #print(first_day["humidity"])
                #tip = transport_tip(first_day["temp"], first_day["humidity"], first_day["wind_kph"], first_day["rainfall"], first_day["condition"])
                render_template('agriculture.html', city=city, forecast=forecast_data, tips=tips, first_day=first_day, tip=tip, days=days)
            else:
                print("Failed to get data from WeatherAPI:", response.status_code)
                flash("Failed to get data from WeatherAPI:"+ str(response.status_code))
                return redirect(url_for('forecast.agriculture'))

        except Exception as e:
            print("Error calling Weather API:", e)
            flash("Error calling Weather API:" + str(e))
            return redirect(url_for('forecast.agriculture'))
    return render_template('agriculture.html', city=city, forecast=forecast_data, tips=tips, first_day=first_day, tip=tip, days=days)



@forecast_bp.route('/mining', methods=['GET', 'POST'])
@login_required
def mining():
    forecast_data = []
    tips = []
    city = ""
    day=None
    first_day = [] 
    tip=""
    days = 0

    if request.method == 'POST':
        city = request.form.get('city')
        days = request.form.get('days', type=int)

        try:
            response = get_weather_forecast(city, days)
            if response.status_code == 200:
                data = response.json()
                for day in data["forecast"]["forecastday"]:
                    entry = {
                        "date": day["date"],
                        "temp": round(day["day"]["avgtemp_c"], 1),
                        "rainfall": round(day["day"]["totalprecip_mm"], 1),
                        "humidity": round(day["day"]["avghumidity"], 1),
                        "condition": day["day"]["condition"]["text"],
                        "wind_kph": day["day"]["maxwind_kph"],
                        "vis_km": day["day"]["avgvis_km"],
                        "chance_of_rain": day["day"]["daily_chance_of_rain"],
                    }
                    forecast_data.append(entry)
                    #tip = mining_tip(round(day["day"]["avgtemp_c"], 1), round(day["day"]["avghumidity"], 1),)
                first_day = forecast_data[0]
                print(first_day["humidity"])
                tip = mining_tip(first_day["temp"], first_day["humidity"], first_day["wind_kph"], first_day["rainfall"], first_day["condition"])
                render_template('mining.html', city=city, forecast=forecast_data, tips=tips, first_day=first_day, tip=tip)
            else:
                print("Failed to get data from WeatherAPI:", response.status_code)
                flash("Failed to get data from WeatherAPI:"+ str(response.status_code))
                return redirect(url_for('forecast.mining'))

        except Exception as e:
            print("Error calling Weather API:", e)
            flash("Error calling Weather API:")
            return redirect(url_for('forecast.mining'))
    return render_template('mining.html', city=city, forecast=forecast_data, tips=tips, first_day=first_day, tip=tip, days=days)


@forecast_bp.route('/aviation', methods=["GET", "POST"])
@login_required
def aviation():
    forecast_data = []
    tips = []
    city = ""
    day=None
    first_day = [] 
    tip=""
    days = ""

    if request.method == 'POST':
        city = request.form.get('city')
        days = request.form.get('days', type=int)

        try:
            response = get_weather_forecast(city, days)
            if response.status_code == 200:
                data = response.json()
                for day in data["forecast"]["forecastday"]:
                    entry = {
                        "date": day["date"],
                        "temp": round(day["day"]["avgtemp_c"], 1),
                        "rainfall": round(day["day"]["totalprecip_mm"], 1),
                        "humidity": round(day["day"]["avghumidity"], 1),
                        "condition": day["day"]["condition"]["text"],
                        "wind_kph": day["day"]["maxwind_kph"],
                        "vis_km": day["day"]["avgvis_km"],
                        "chance_of_rain": day["day"]["daily_chance_of_rain"],
                    }
                    forecast_data.append(entry)
                    #tip = mining_tip(round(day["day"]["avgtemp_c"], 1), round(day["day"]["avghumidity"], 1),)
                first_day = forecast_data[0]
                #print(first_day["humidity"])
                tip = aviation_tip(first_day["temp"], first_day["humidity"], first_day["wind_kph"], first_day["vis_km"], first_day["rainfall"], first_day["condition"])
                render_template('aviation.html', city=city, forecast=forecast_data, tips=tips, first_day=first_day, tip=tip, days=days)
            else:
                print("Failed to get data from WeatherAPI:", response.status_code)
                flash("Failed to get data from WeatherAPI:"+ str(response.status_code))
                return redirect(url_for('forecast.aviation'))

        except Exception as e:
            print("Error calling Weather API:", e)
            flash("Error calling Weather API:")
            return redirect(url_for('forecast.aviation'))
    return render_template('aviation.html', city=city, forecast=forecast_data, tips=tips, first_day=first_day, tip=tip, days=days)


@forecast_bp.route('/transportation', methods=["GET", "POST"])
@login_required
def transportation():
    forecast_data = []
    tips = []
    city = ""
    day=None
    first_day = [] 
    tip=""
    days = ""

    if request.method == 'POST':
        city = request.form.get('city')
        days = request.form.get('days', type=int)

        try:
            response = get_weather_forecast(city, days)
            if response.status_code == 200:
                data = response.json()
                for day in data["forecast"]["forecastday"]:
                    entry = {
                        "date": day["date"],
                        "temp": round(day["day"]["avgtemp_c"], 1),
                        "rainfall": round(day["day"]["totalprecip_mm"], 1),
                        "humidity": round(day["day"]["avghumidity"], 1),
                        "condition": day["day"]["condition"]["text"],
                        "wind_kph": day["day"]["maxwind_kph"],
                        "vis_km": day["day"]["avgvis_km"],
                        "chance_of_rain": day["day"]["daily_chance_of_rain"],
                    }
                    forecast_data.append(entry)
                    #tip = mining_tip(round(day["day"]["avgtemp_c"], 1), round(day["day"]["avghumidity"], 1),)
                first_day = forecast_data[0]
                #print(first_day["humidity"])
                tip = transport_tip(first_day["temp"], first_day["humidity"], first_day["wind_kph"], first_day["rainfall"], first_day["condition"])
                render_template('transportation.html', city=city, forecast=forecast_data, tips=tips, first_day=first_day, tip=tip, days=days)
            else:
                print("Failed to get data from WeatherAPI:", response.status_code)
                flash("Failed to get data from WeatherAPI:"+ str(response.status_code))
                return redirect(url_for('forecast.transportation'))

        except Exception as e:
            print("Error calling Weather API:", e)
            flash("Error calling Weather API:")
            return redirect(url_for('forecast.transportation'))
    return render_template('transportation.html', city=city, forecast=forecast_data, tips=tips, first_day=first_day, tip=tip, days=days)
