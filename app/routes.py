from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('Form has been validated! Yippy Kai Yay')
        email = form.email.data
        username = form.username.data
        password = form.password.data
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user:
            flash('A user with that username or email already exists.', 'danger')
            return redirect(url_for('signup'))
            
        new_user = User(email=email, username=username, password=password)
        flash(f"{new_user.username} has been created.", "success")
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            login_user(user)
            flash(f"Welcome back {user.username}!", "success")
            return redirect(url_for('index'))
        else:
            flash("Incorrect username and/or password. Please try again.", 'danger')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out.', 'primary')
    return redirect(url_for('index'))

@app.route('/delete', methods=['GET', 'POST'])
@login_required
def delete_user(self):
    if self.author != current_user:
        flash("You do not have permission to delete this account", "danger")
        return redirect(url_for('index'))
    self.delete()
    flash(f'{self.user} has been deleted', 'info')
    return redirect(url_for('index'))