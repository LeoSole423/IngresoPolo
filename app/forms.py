from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message="Por favor, ingresa un email válido")
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(),
        Length(min=6, message="La contraseña debe tener al menos 6 caracteres")
    ])
    submit = SubmitField('Iniciar sesión')

class RegisterForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[
        DataRequired(),
        Length(min=3, max=20, message="El nombre de usuario debe tener entre 3 y 20 caracteres")
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message="Por favor, ingresa un email válido")
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(),
        Length(min=6, message="La contraseña debe tener al menos 6 caracteres")
    ])
    confirm_password = PasswordField('Confirmar contraseña', validators=[
        DataRequired(),
        EqualTo('password', message="Las contraseñas no coinciden")
    ])
    submit = SubmitField('Registrarse')

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        return True
