from app import app, db

# Crear las tablas en la base de datos
db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
