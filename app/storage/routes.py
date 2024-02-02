from app.storage import storage_bp
from flask_login import login_required,logout_user
from flask import render_template,redirect,url_for,g,request
from flask_login import current_user
from app.storage.form import PasswordForm,DataPasswordForm
from app.system_db.password import Password
from app.storage._jwt import generate_token,decode_token

@storage_bp.route('/')
@login_required
def redirect_storage():
    return redirect(url_for('storage_bp.storage',username=current_user.username))
@storage_bp.route('/storage/<username>',methods=['GET','POST'])
@login_required
def storage(username,page=1):
    if request.args.get('page'):
        page = request.args.get('page')
    g.generate_token = generate_token
    form = PasswordForm()
    data = Password.get(user_id=current_user.user_id,page=int(page))
    pages = Password.get_count_group(current_user.user_id)
    if form.validate_on_submit():
        title = form.title.data
        password = form.password.data
        Password.add(title,password,current_user.user_id)
        return redirect(url_for('storage_bp.storage',username=username))
    return render_template('storage/storage.html',form=form,data=data,pages=pages,page=int(page))

@storage_bp.route('/storage/<username>/password',methods=['GET','POST'])
@login_required
def storage_password(username):
    form = DataPasswordForm()
    token = request.args.get('password_id')
    data = decode_token(token)
    password_id = data['password_id']
    password = Password.get_password(password_id)
    if form.validate_on_submit():
        title = form.title.data
        password_ = form.password.data
        Password.update_password_data(password_id,password_,title)
        return redirect(url_for('storage_bp.storage',username=username))
    form.title.data = password.title
    form.password.data = password.password
    return render_template('storage/password.html',password=password,form=form)

@storage_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))
