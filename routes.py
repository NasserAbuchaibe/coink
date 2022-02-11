import logging

from flask import flash, redirect, render_template, request, url_for
from sqlalchemy import exc

from app import app, db
from forms import LoginForm
from models import Usuario
from services import logs

logger = logging.getLogger(__name__)


@app.errorhandler(404)
def page_not_found(error):
    """[Capture 404 error and render corresponding template]

    Args:
        error ([error]): [error 404]

    Returns:
        [template]: [404.html]
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """[Capture 500 error and render corresponding template]

    Args:
        error ([error]): [error 500]

    Returns:
        [template]: [500.html]
    """
    return render_template('500.html'), 500


@app.route('/list')
def list_all():
    """[Check all the database records and render the template with the information]

    Returns:
        [template]: [template with the records consulted]
    """
    users = Usuario.query.all()
    return render_template('list.html', users=users)


@app.route('/', methods=['GET', 'POST'])
def index():
    """[Render main page and capture information to save in the database]

    Returns:
        [template]: [template with form]
    """

    login_form = LoginForm()

    # Validation of the form data
    if login_form.validate_on_submit():
        try:
            # Get an instance of the User model
            user = prepare_user_to_db(
                request.form['username'], request.form['email'], request.form['city'])

            # Creating user in the database
            save_data(user)
            flash('Registro creado')
        except SystemError as err:
            logger.error("Error %s", str(err))

        return redirect(url_for('index'))

    context = {
        'login_form': login_form
    }
    return render_template('index.html', **context)


def save_data(user):
    """[Insert data into the database and call the function that generates logs]

    Args:
         user ([object]): [Usuario model instance]

    Raises:
        SystemError: [error message when creating new record in database]
    """
    try:
        db.session.add(user)
        db.session.commit()

        # Log user creation event
        logs(user)

        logger.info("Se ha creado un usuario con los siguientes datos %s", user)
    except exc.SQLAlchemyError as err:
        raise SystemError(f"Ocurrio un error al guardar la data {str(err)}")


def prepare_user_to_db(username, email, city):
    """[creates an instance of the Usuario model]

    Args:
        username ([str]): [User name]
        email ([str]): [Email user]
        city ([str]): [user's city]

    Returns:
        [object]: [Usuario model instance]
    """
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
