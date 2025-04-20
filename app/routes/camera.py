from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

camera_bp = Blueprint('camera', __name__, url_prefix='/camera')

@camera_bp.route('/', methods=['GET'])
@login_required
def camera_home():
    # Aquí se listarán las cámaras del usuario
    return render_template('camera/home.html')

@camera_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_camera():
    if request.method == 'POST':
        # Aquí se procesará el formulario para agregar una cámara
        flash('Funcionalidad en desarrollo', 'info')
        return redirect(url_for('camera.camera_home'))
    return render_template('camera/add.html')
