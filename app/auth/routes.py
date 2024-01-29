from flask import render_template,redirect,url_for,flash,request
from app.auth import auth_bp
from flask_login import current_user,login_user
from app.system_db.users import Users
from app.auth.form import LoginForm,RegisterForm,ResetPasswordForm,NewPasswordForm
from app.auth._jwt import generate_token,decode_token
from app.auth.messages import send_jwt

@auth_bp.route('/',methods=['GET','POST'])
def login():
    if current_user.is_anonymous:
        form = LoginForm()
        if request.method == 'POST':
            username = form.username.data
            password = form.password.data
            remember_me = form.remember_me.data
            user = Users.get_instance(username,password)
            if user:
                login_user(user,remember=remember_me)
                return redirect(url_for('storage_bp.storage',username=current_user.username))
            flash('Данные не коректны')
        return render_template('auth/login.html',form=form)
    return redirect(url_for('storage_bp.storage',username=current_user.username))

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_anonymous:
        form = RegisterForm()
        if request.method == 'POST':
            username = form.username.data
            password = form.password.data
            email = form.email.data
            if Users.add(username,password,email):
                user = Users.get_instance(username,password)
                remember_me = form.remember_me.data
                login_user(user,remember=remember_me)
                return redirect(url_for('storage_bp.storage',username=current_user.username))
            flash('Такой пользователь уже существует')
        return render_template('auth/register.html',form=form)
    return redirect(url_for('storage_bp.storage',username=current_user.username))

@auth_bp.route('/reset_password',methods=['GET','POST'])
def reset_password():
    if current_user.is_anonymous:
        form = ResetPasswordForm()
        if form.validate_on_submit():
            email = form.email.data
            user_id = Users.check_email(email)
            if user_id:
                token = generate_token(user_id)
                send_jwt(email,token)
                flash('Проверьте вашу почту')
        return render_template('auth/reset_password.html',form=form)
    return redirect(url_for('storage_bp.storage'))

@auth_bp.route('/reset_password/new_password',methods=['GET','POST'])
def new_password():
    if current_user.is_anonymous:
        form = NewPasswordForm()
        token = request.args.get('token')
        data = decode_token(token)
        user_id = data['user_id']
        if form.validate_on_submit():
            password = form.password.data
            Users.update_password(user_id=user_id,password=password)
            return redirect(url_for('auth_bp.login'))
        return render_template('auth/new_password.html',form=form)
    return redirect(url_for('storage_bp.storage'))
