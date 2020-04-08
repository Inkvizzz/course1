from app import app, db
from flask import render_template, redirect, url_for, flash, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Store, Book
from werkzeug.urls import url_parse


@app.route('/', methods=['GET'])
@app.route('/home/', methods=['GET'])
@login_required
def home():
    return render_template('home.html')

@app.route('/home/<storename>', methods=['GET'])
def store(storename):
    books = Book.query.all()
    return render_template('home.html', books=books)


@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Store(inn=form.username.data, email=form.email.data)
        user.set_password(form.password2.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Store.query.filter_by(inn = form.username.data).first()
        if user is None:
            flash('Invalid username. Try login again')
            return redirect(url_for('login'))
        elif not user.check_password(form.password.data):
            flash('Invalid password. Try login again')
            return redirect(url_for('login'))
        else:
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('home')
            return redirect(next_page)


        return redirect(url_for('home'))

    return render_template('login.html', title="Auth page", form=form)

@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))