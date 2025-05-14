# Tareas App

Este proyecto es una aplicación web de gestión de tareas, desarrollada en Flask, que permite a los usuarios iniciar sesión, agregar, editar, completar y eliminar tareas personales.

## Características

- Registro e inicio de sesión de usuarios.
- Creación de tareas con título y descripción.
- Marcado de tareas como completadas.
- Eliminación de tareas.
- Base de datos SQLite para almacenar usuarios y tareas.

## Requerimientos

Para ejecutar este proyecto, necesitas tener Python 3.x y las siguientes librerías instaladas:
- Flask
- Flask-Login
- SQLite3
- Werkzeug

Puedes instalar las dependencias necesarias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu_usuario/tareas-app.git
cd tareas-app
```

2. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Inicia la aplicación:
```bash
python app.py
```

La aplicación estará disponible en http://127.0.0.1:5000/.

## Autor

Freddy Yujra Mamani  
Correo: Freddyuj0@gmail.com
