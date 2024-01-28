from flask import render_template,redirect,url_for,flash,request
from app.auth import auth_bp
from flask_login import current_user,login_user
from app.system_db.users import Users
from app.auth.form import LoginForm,RegisterForm

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
                return redirect(url_for('storage.storage',username=current_user.username))
            flash('Данные не коректны')
        return render_template('auth/login.html',form=form)
    return redirect(url_for('storage.storage',username=current_user.username))

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
                return redirect(url_for('storage.storage',username=current_user.username))
            flash('Такой пользователь уже существует')
        return render_template('auth/register.html',form=form)
    print(current_user.username)
    return redirect(url_for('storage.storage',username=current_user.username))

