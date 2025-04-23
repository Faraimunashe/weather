from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from passlib.hash import sha256_crypt
from app import db
from app.models import User

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if not sha256_crypt.verify(current_password, current_user.password):
            flash('Current password is incorrect.', 'error')
            return redirect(url_for('profile.profile'))

        if new_password != confirm_password:
            flash('New passwords do not match.', 'error')
            return redirect(url_for('profile.profile'))

        current_user.password = sha256_crypt.encrypt(new_password)
        db.session.commit()

        flash('Password changed successfully!', 'success')
        return redirect(url_for('profile.profile'))

    return render_template('profile.html')
