from app.storage import storage_bp
from flask_login import login_required,logout_user
from flask import render_template,redirect,url_for,g,request
from flask_login import current_user
from app.storage.form import PasswordForm
from app.system_db.password import Password
from app.storage._jwt import generate_token,decode_token

@storage_bp.route('/')
@login_required
def redirect_storage():
    return redirect(url_for('storage_bp.storage',username=current_user.username))
@storage_bp.route('/storage/<username>',methods=['GET','POST'])
@login_required
def storage(username):
    g.generate_token = generate_token
    form = PasswordForm()
    if form.validate_on_submit():
        title = form.title.data
        password = form.password.data
        Password.add(title,password,current_user.user_id)
        return redirect(url_for('storage_bp.storage',username=username))
    data = Password.get(user_id=current_user.user_id,page=1)
    return render_template('storage/storage.html',form=form,data=data)

@storage_bp.route('/storage/<username>/password')
@login_required
def storage_password(username):
    token = request.args.get('password_id')
    data = decode_token(token)
    password_id = data['password_id']
    password = Password.get_password(password_id)
    return render_template('storage/password.html',password=password)

@storage_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))
