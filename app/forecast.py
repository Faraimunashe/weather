from flask import Blueprint, render_template
from flask_login import login_required
from . import db
from app.models import User
from datetime import datetime, date

forecast_bp = Blueprint('forecast', __name__)

@forecast_bp.route('/forecast', methods=['GET', 'POST'])
#@login_required
def forecast():
    
    return render_template('forecast.html')



@forecast_bp.route('/agriculture')
def agriculture():
    return render_template('agriculture.html')


@forecast_bp.route('/mining')
def mining():
    return render_template('mining.html')

@forecast_bp.route('/aviation')
def aviation():
    return render_template('aviation.html')

@forecast_bp.route('/transportation')
def transportation():
    return render_template('transportation.html')