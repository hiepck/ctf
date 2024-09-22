from flask import Flask, render_template, request, redirect, url_for, session
import redis
import os

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()

db = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

FLAG = open("/flag.txt", "rb").read().strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username is 'admin'
        if username.lower() == 'cookiehanhoan':
            return 'You cannot create a user with the username "cookiehanhoan"!'

        if db.hgetall(username):
            return 'Username already exists!'
        db.hset(username, mapping={'password': password})
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.hgetall(username)

        # Check if the username is 'cookiehanhoan'
        if username == 'cookiehanhoan' and user and user['password'] == password:
            session['username'] = username
            return FLAG

        if user and user['password'] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return 'Invalid credentials!'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run("0.0.0.0", 1330)

