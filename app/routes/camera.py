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

@camera_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_camera():
    if request.method == 'POST':
        name = request.form.get('name')
        cam_type = request.form.get('type')
        ip = request.form.get('ip')
        port = request.form.get('port')
        username = request.form.get('username')
        password = request.form.get('password')
        stream_url = request.form.get('stream_url') if cam_type == 'DIRECT' else None
        camera = Camera(
            user_id=current_user.get_id(),
            name=name,
            type=cam_type,
            ip=ip,
            port=port,
            username=username,
            password=password,
            stream_url=stream_url
        )
        db.session.add(camera)
        db.session.commit()
        flash('Cámara agregada correctamente', 'success')
        return redirect(url_for('camera.camera_home'))
    return render_template('camera/add.html')

@camera_bp.route('/view/<int:camera_id>')
@login_required
def view_camera(camera_id):
    camera = Camera.query.get_or_404(camera_id)
    if camera.user_id != int(current_user.get_id()):
        flash('No tienes permiso para ver esta cámara', 'danger')
        return redirect(url_for('camera.camera_home'))
    # Si es directa y tiene stream_url, mostrarlo
    return render_template('camera/view.html', camera=camera)
