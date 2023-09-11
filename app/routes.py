from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user
from dilemma_list import add_dilemmas

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ponder')
def ponder():
    return render_template('ponder.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        check_user = db.session.execute(db.select(User).where( (User.username==username) | (User.email==email) )).scalar()
        if check_user:
            flash('A user with that username and/or email already exists', 'danger')
            return redirect(url_for('signup'))
        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'{new_user.username} has been created', 'success')
        login_user(new_user)
        return redirect(url_for('index'))
    elif form.is_submitted():
        flash("Your passwords do not match", 'danger')
        return redirect(url_for('signup'))
    
    return render_template('signup.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("You have successfully logged out", "danger")
    return redirect(url_for('index'))


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = db.session.execute(db.select(User).where(User.username==username)).scalar()
        if user is not None and user.check_password(password):
            login_user(user)
            flash("You have successfully logged in", 'primary')
            return redirect(url_for('index'))
        else:
            flash('Invalid username and/or password', 'danger')
            return redirect(url_for('login'))
            
    return render_template('login.html', form=form)

@app.route('/hidden')
def hidden():
    add_dilemmas()