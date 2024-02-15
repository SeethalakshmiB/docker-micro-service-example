from flask import Flask, render_template, request, redirect, session, flash
# from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import os
import boto3


# basedir = os.path.abspath(os.path.dirname(__file__))
db_user_name = os.environ['DB_USERNAME']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
db_host = os.environ['DB_HOST']

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user_name}:{db_password}@{db_host}/{db_name}'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

secret_name = "abc-secret"

# Secret key for session management
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    # Create all tables if they do not exist
    db.create_all()
    print('Tables created successfully!')
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        new_user = User(username, hashed_password)

        db.session.add(new_user)

        db.session.commit()

        flash('Registration successful! Please login.')
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user:
            print(user)
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                session['loggedin'] = True
                
                session['username'] = user.username
                flash('Login successful!')
                return redirect('/profile')
            else:
                flash('Invalid username or password. Please try again.')
        else:
            flash('Invalid username or password. Please try again.')

    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'loggedin' in session:
        return render_template('profile.html', username=session['username'])
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    flash('You have been logged out successfully.')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
