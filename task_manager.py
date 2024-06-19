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


# Add Task Page
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        conn = sqlite3.connect('tasks.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template('add.html')


# Edit Task Page
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        cur.execute("UPDATE tasks SET title = ?, description = ? WHERE id = ?", (title, description, id))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    else:
        cur.execute("SELECT * FROM tasks WHERE id = ?", (id,))
        task = cur.fetchone()
        conn.close()
        return render_template('edit.html', task=task)


# Delete Task
@app.route('/delete/<int:id>', methods=['GET'])
def delete_task(id):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))


# Main
if __name__ == '__main__':
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
