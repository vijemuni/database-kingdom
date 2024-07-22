from flask import Flask, render_template, request, redirect, url_for, flash, session
from pymongo import MongoClient
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.urandom(24)

# MongoDB connection
client = MongoClient("mongodb+srv://paperskingdom:xxxtentacion4321@cluster0.jpidcjk.mongodb.net/paperskingdom?retryWrites=true&w=majority")
db = client['paperskingdom']
collection = db['papers-kingdom-collection']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if username and email and password:
            hashed_password = generate_password_hash(password)
            collection.insert_one({'username': username, 'email': email, 'password': hashed_password})
            flash('Sign-up successful! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('All fields are required.', 'danger')

    return render_template('sign-up.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = collection.find_one({'email': email})

        if user and check_password_hash(user['password'], password):
            session['user'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
