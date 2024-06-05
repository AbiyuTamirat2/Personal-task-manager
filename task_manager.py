from flask import Flask, request, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, 
    description TEXT)''')
    conn.close()

# Home Page: Display all tasks
@app.route('/')
def home():
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    conn.close()
    return render_template('home.html', tasks=tasks)
@app.route('/')
def home():
    return "Welcome to the Personal Task Manager!"

# Main
if __name__ == '__main__':
    app.run(debug=True)