from app import app, db
from flask import render_template, redirect, url_for, flash, make_response, request
from app.forms import SignUpForm, LoginForm
from app.models import User, Dilemma
from flask_login import login_user, logout_user, login_required, current_user
from app.dilemma_list import add_dilemmas
from random import randint
import wikipedia

@app.route('/')
def index():
    if current_user.is_authenticated == True:
        return redirect('/ponder')
    else:
        title = Dilemma.query.filter_by(id=randint(1,23)).first().title
        return render_template('index.html', title=title)

@app.route('/ponder', methods=["GET", "POST"])
@login_required
def ponder():
    if current_user.last_dilemma > db.session.query(Dilemma).count():
        dilemma = Dilemma.query.filter_by(id=24).first()
    else:
        dilemma = Dilemma.query.filter_by(id=current_user.last_dilemma).first()

    if request.method == 'POST':
        if 'choice_a' in request.form:
            current_user.c_score += dilemma.c_score
            current_user.d_score += dilemma.d_score
            current_user.v_score += dilemma.v_score
            current_user.n_score += dilemma.n_score
        if 'choice_b' in request.form:
            current_user.c_score -= dilemma.c_score
            current_user.d_score -= dilemma.d_score
            current_user.v_score -= dilemma.v_score
            current_user.n_score -= dilemma.n_score

        current_user.last_dilemma += 1
        db.session.commit()
        return redirect('/ponder')
    else:
        return render_template('ponder.html', dilemma=dilemma)

@app.route('/profile', methods=["GET", "POST"])
def profile():
    scores = {'consequentialism':current_user.c_score,'deontology':current_user.d_score,'virtue_ethics':current_user.v_score,'nihilism':current_user.n_score}
    max_score = scores['consequentialism']
    ethic = 'consequentialism'
    for _ethic, score in scores.items():
        if score > max_score:
            ethic = _ethic
            max_score = score
    pract = {'consequentialism': ['niccolò machiavelli', 'jeremy bentham', 'peter singer'],
    'deontology': ['immanuel kant', 'w. d. ross', 't. m. scanlon'],
    'virtue_ethics': ['aristotle', 'thomas aquinas', 'elizabeth anscombe'],
    'nihilism': ['friedrich Heinrich Jacobi', 'søren Kierkegaard', 'friedrich nietzsche']}

    return render_template('profile.html', ethic=ethic, pract=pract, wikipedia=wikipedia)

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
        return redirect(url_for('ponder'))
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
            return redirect(url_for('ponder'))
        else:
            flash('Invalid username and/or password', 'danger')
            return redirect(url_for('login'))
            
    return render_template('login.html', form=form)

@app.route('/hidden')
def hidden():
    add_dilemmas()
    return make_response('hello')

@app.route('/reset')
def reset():
    print(current_user.c_score)
    current_user.last_dilemma = 1
    current_user.c_score = 0
    current_user.d_score = 0
    current_user.v_score = 0
    current_user.n_score = 0
    db.session.commit()
    return redirect(url_for('ponder'))