# Flask MySQL Task Manager

Aplicación web para la gestión de tareas con autenticación de usuarios, desarrollada con Flask y MySQL, y una interfaz responsiva basada en Bootstrap.

## Características

- Registro, inicio y cierre de sesión de usuarios
- Gestión de tareas: crear, ver, editar y eliminar
- Interfaz responsiva con Bootstrap
- Integración con base de datos MySQL
- Organización modular del código con Blueprints y modelos
- Acceso a cámaras IP a través del protocolo ONVIF (en desarrollo)

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
   - Copia el archivo `.env.example` y renómbralo como `.env`.
   - Completa los valores requeridos para cada variable según tu entorno local.
   - **No subas tu archivo `.env` al repositorio, ya que contiene información sensible.**

   El archivo `.env.example` contiene un ejemplo de las variables necesarias:
   ```env
   MYSQL_ROOT_PASSWORD=your_mysql_root_password
   MYSQL_DATABASE=your_database_name
   DATABASE_URL=mysql+pymysql://root:your_mysql_root_password@db:3306/your_database_name
   SECRET_KEY=your_secret_key
   ```
   Cambia estos valores en tu `.env` real según tus credenciales y entorno.

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

## Flujo de trabajo con ramas

- `main`: Rama estable, lista para producción. Solo recibe cambios probados y listos.
- `develop`: Rama de integración donde se desarrollan y prueban nuevas funcionalidades.
- `feature/nombre-feature`: Para cada nueva funcionalidad, crea una rama desde `develop` y trabaja ahí. Cuando termines, haz merge a `develop`.

**Ejemplo de contribución:**
```bash
git checkout develop
git pull origin develop
git checkout -b feature/nueva-funcionalidad
# Realiza tus cambios y haz commits
# Cuando termines:
git add .
git commit -m "Describe tu cambio"
git push origin feature/nueva-funcionalidad
# Haz un Pull Request a develop
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