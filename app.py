from flask import Flask, render_template, request, redirect, url_for,flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'ClaveSuperSecreta'

# Configurar Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Obtener conexion a la base de datos
def get_db_conection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Inicializar base de datos
def Init_db():
    conn = get_db_conection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

# Clase Usuario para Flask-Login
class User(UserMixin):
    def __init__(self, id, username, password, name = None, email = None):
        self.id = id
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    @staticmethod
    def get_by_id(user_id):
        conn = get_db_conection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id)).fetchone()       
        conn.close()
        if user:
            return User(user['id'], user['username'], user['password'], user['name'], user['email'])
        return None

    @staticmethod
    def get_by_username(username):
        conn = get_db_conection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        if user:
            return User(user['id'], user['username'], user['password'], user['name'], user['email'])
        return None

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        hash_pass = generate_password_hash(password)
        
        conn = get_db_conection()
        try:
            conn.execute(
                'INSERT INTO users (name, email, username, password) VALUES(?,?,?,?)',
                (name, email, username, hash_pass)
            )
            conn.commit()
            flash('Usuario registrado correctamente. Inicia sesión.','success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('El nombre de usuario ya existe.','danger')
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.get_by_username(username)
        if user and check_password_hash(user.password, password):       
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales inválidos', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username = current_user.username, name = current_user.name)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    Init_db()
    app.run(debug=True)