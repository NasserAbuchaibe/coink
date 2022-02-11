import logging

from flask import redirect, render_template, request, url_for, flash
from sqlalchemy import exc

from app import app, db
from forms import LoginForm
from models import Usuario
from services import logs

logger = logging.getLogger(__name__)


@app.route('/list')
def list_all():
    users = Usuario.query.all()
    return render_template('list.html', users=users)


@app.route('/', methods=['GET', 'POST'])
def index():

    login_form = LoginForm()

    if login_form.validate_on_submit():
        try:
            user = prepare_user_to_db(
                request.form['username'], request.form['email'], request.form['city'])
            save_data(user)
            flash('Registro creado')
        except SystemError as err:
            logger.error("Error %s", str(err))
            """Return "error"""
        return redirect(url_for('index'))

    context = {
        'login_form': login_form
    }
    return render_template('index.html', **context)


def save_data(user):
    try:
        db.session.add(user)
        db.session.commit()
        logs(user)
        logger.info("Se ha creado un usuario con los siguientes datos %s", user)
    except exc.SQLAlchemyError as err:
        raise SystemError(f"Ocurrio un error al guardar la data {str(err)}")


def prepare_user_to_db(username, email, city):
    try:
        user = Usuario(
            username=username,
            email=email,
            city=city
        )
    except exc.SQLAlchemyError as err:
        raise SystemError(
            f"Ocurrio un error al preparar la data de usuario {str(err)}")
    return user

