from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.camera import Camera
from app import db

camera_bp = Blueprint('camera', __name__, url_prefix='/camera')

@camera_bp.route('/', methods=['GET'])
@login_required
def camera_home():
    cameras = Camera.query.filter_by(user_id=current_user.get_id()).all()
    return render_template('camera/home.html', cameras=cameras)

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Optional

class CameraForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    type = SelectField('Tipo de cámara', choices=[('ONVIF', 'ONVIF'), ('DIRECT', 'Directa (HTTP/MJPEG)')], validators=[DataRequired()])
    ip = StringField('Dirección IP', validators=[DataRequired()])
    port = IntegerField('Puerto', validators=[Optional()])
    username = StringField('Usuario', validators=[Optional()])
    password = PasswordField('Contraseña', validators=[Optional()])
    stream_url = StringField('URL de stream HTTP/JPEG/MJPEG', validators=[Optional()])

@camera_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_camera():
    form = CameraForm()
    if form.validate_on_submit():
        from werkzeug.security import generate_password_hash
        hashed_password = generate_password_hash(form.password.data) if form.password.data else None
        camera = Camera(
            user_id=current_user.get_id(),
            name=form.name.data,
            type=form.type.data,
            ip=form.ip.data,
            port=form.port.data,
            username=form.username.data,
            password=hashed_password,
            stream_url=form.stream_url.data if form.type.data == 'DIRECT' else None
        )
        db.session.add(camera)
        db.session.commit()
        flash('Cámara agregada correctamente', 'success')
        return redirect(url_for('camera.camera_home'))
    return render_template('camera/add.html', form=form)

@camera_bp.route('/view/<int:camera_id>')
@login_required
def view_camera(camera_id):
    camera = Camera.query.get_or_404(camera_id)
    if camera.user_id != int(current_user.get_id()):
        flash('No tienes permiso para ver esta cámara', 'danger')
        return redirect(url_for('camera.camera_home'))
    # Si es directa y tiene stream_url, mostrarlo
    return render_template('camera/view.html', camera=camera)
