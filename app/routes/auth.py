from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app import db, forms
from app.forms import LoginForm, RegisterForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            return redirect(url_for('main.index'))
        flash('Credenciales incorrectas. Por favor intenta nuevamente.')
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        try:
            # Intentar validar el formulario
            if form.validate():
                # Verificar si el email ya existe
                existing_user = User.query.filter_by(email=form.email.data).first()
                if existing_user:
                    flash('El email ya está registrado.')
                    return render_template('auth/register.html', form=form)

                # Crear nuevo usuario
                new_user = User(
                    username=form.username.data,
                    email=form.email.data,
                    password=generate_password_hash(form.password.data, method='sha256')
                )
                db.session.add(new_user)
                try:
                    db.session.commit()
                    flash('¡Cuenta creada con éxito!')
                    return redirect(url_for('auth.login'))
                except Exception as e:
                    db.session.rollback()
                    flash('Error al crear la cuenta. Por favor, intenta nuevamente.')
                    print(f"Error: {str(e)}")
            else:
                # Mostrar errores de validación
                for field, errors in form.errors.items():
                    for error in errors:
                        flash(f'Error en {getattr(form, field).label.text}: {error}', 'error')
        except Exception as e:
            flash('Error de validación. Por favor, intenta nuevamente.')
            print(f"Error: {str(e)}")
    
    return render_template('auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
