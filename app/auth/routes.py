from flask import Blueprint, render_template, request

from .forms import UserCreationForm
from app.models import User

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/login')
def loginPage():
    return render_template('login.html')

@auth.route('/signup', methods=["GET", "POST"])
def signupPage():
    form = UserCreationForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            print(username, email, password)

            user = User(username, email, password)
            
            user.saveToDB()

    return render_template('signup.html', form=form)

