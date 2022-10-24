from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_user, logout_user, current_user
from .forms import LoginForm, UserForm
from app.models import User
from werkzeug.security import check_password_hash
from email_validator import validate_email, EmailSyntaxError

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/login', methods=["GET", "POST"])
def loginPage():
    form = LoginForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    print('Successfully Logged In')
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    print('That is not your password!!!')
            else:
                print('This user does not exist. Please try again...')
    return render_template('login.html', form=form)

@auth.route('/signup', methods=["GET", "POST"])
def signupPage():
    form = UserForm()
    if request.method == "POST":
        if form.validate():
            firstname = (form.firstname.data).lower()
            lastname = (form.lastname.data).lower()
            username = form.username.data
            email = form.email.data
            password = form.password.data
            user = User(firstname, lastname, username, email, password)
            try:
                email = validate_email(email)
            except:
                email_error = "That is not a valid email address."
                return render_template('signup.html', form=form, email_error=email_error)
            user.saveToDB()
            return redirect(url_for('auth.loginPage'))
    return render_template('signup.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.loginPage'))

@auth.route('/update')
def updateUser(user_id):
    form = UserForm()
    if request.method == "POST":
        if form.validate():
            firstname = (form.firstname.data).lower()
            lastname = (form.lastname.data).lower()
            username = form.username.data
            email = form.email.data
            password = form.password.data
            user = User(firstname, lastname, username, email, password)
            try:
                email = validate_email(email)
            except:
                email_error = "That is not a valid email address."
                return render_template('signup.html', form=form, email_error=email_error)
            user.saveToDB()
            return redirect(url_for('auth.loginPage'))
    return render_template('update_user.html', form=form)