from app import db
from flask_login import current_user

class Camera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(10), nullable=False)  # 'ONVIF' o 'DIRECT'
    ip = db.Column(db.String(100), nullable=False)
    port = db.Column(db.Integer, nullable=True)
    username = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(100), nullable=True)
    stream_url = db.Column(db.String(255), nullable=True)  # Para cámaras directas

    def is_owner(self):
        return self.user_id == current_user.get_id()
