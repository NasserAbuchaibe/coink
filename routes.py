from crypt import methods
from flask import render_template, request, redirect, url_for
from flask_uuid import FlaskUUID
from flask_wtf import FlaskForm

import config
from app import app, db
from forms import LoginForm
from models import Usuario


@app.route('/', methods=['GET', 'POST'])
def index():

    login_form = LoginForm()

    if login_form.validate_on_submit():

        usuario = Usuario(
        username = request.form['username'],
        email = request.form['email'],
        city = request.form['city']
        )

        db.session.add(usuario)
        db.session.commit()

        return redirect(url_for('index'))

    context = {
        'login_form': login_form
    }
    return render_template('index.html', **context)


@app.route('/list')
def list_all():
    users = Usuario.query.all()
    return render_template('list.html', users=users)