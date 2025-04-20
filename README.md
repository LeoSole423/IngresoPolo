# Flask MySQL Task Manager

Aplicación web para la gestión de tareas con autenticación de usuarios, desarrollada con Flask y MySQL, y una interfaz responsiva basada en Bootstrap.

## Características

- Registro, inicio y cierre de sesión de usuarios
- Gestión de tareas: crear, ver, editar y eliminar
- Interfaz responsiva con Bootstrap
- Integración con base de datos MySQL
- Organización modular del código con Blueprints y modelos

## Estructura del Proyecto

```
Mysqltest/
│
├── app/
│   ├── __init__.py
│   ├── forms.py
│   ├── models/
│   │   ├── user.py
│   │   └── task.py
│   ├── routes/
│   │   ├── main.py
│   │   └── auth.py
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   └── templates/
│       ├── auth/
│       ├── main/
│       └── layout.html
├── config.py
├── .env
├── requirements.txt
├── run.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. **Configura las variables de entorno:**
   - Renombra `.env.example` a `.env` y completa los valores necesarios.

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos MySQL:**
   - Asegúrate de tener MySQL corriendo y actualiza las credenciales en `.env` o `config.py`.

5. **Inicializa la base de datos:**
   ```bash
   flask db upgrade
   ```

6. **Ejecuta la aplicación:**
   ```bash
   flask run
   ```
   O usando Docker:
   ```bash
   docker-compose up --build
   ```

## Uso

- Accede a `http://localhost:5000` en tu navegador.
- Regístrate, inicia sesión y comienza a gestionar tus tareas.

## Tecnologías utilizadas

- Python 3.x
- Flask
- MySQL
- SQLAlchemy
- WTForms
- Bootstrap 4/5
- Docker (opcional)

## Licencia

Este proyecto está bajo la licencia MIT.