from flask import Blueprint, render_template
from flask_login import login_required
from . import db
from app.models import User
from datetime import datetime, date

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    
    return render_template('feedback.html')
