from app.storage import storage_bp
from flask_login import login_required,logout_user
from flask import render_template,redirect,url_for

@storage_bp.route('/<username>')
@login_required
def storage(username):
    return render_template('storage/storage.html')

@storage_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))