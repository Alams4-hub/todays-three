import sqlite3
from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn



def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_text TEXT NOT NULL,
            task_date TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
    
    
def add_task(task_text, task_date):
    conn = get_db()
    conn.execute("""INSERT INTO tasks (task_text, task_date) VALUES (?, ?)""", (task_text, task_date))
    conn.commit()
    conn.close()
    
    
def get_todays_tasks():
    today = date.today().isoformat()
    conn = get_db()
    row = conn.execute("SELECT * FROM tasks WHERE task_date = ?", (today,)).fetchall()
    conn.close()
    return row


@app.route("/", methods=["GET", "POST"])
def home():
    task1 = ""
    task2 = ""
    task3 = ""
    
    if request.method == "POST":
        task1 = request.form["task1"]
        task2 = request.form["task2"]
        task3 = request.form["task3"]
        print(task1, task2, task3)
        today = date.today().isoformat()
        add_task(task1, today)
        add_task(task2, today)
        add_task(task3, today)
    tasks = get_todays_tasks()    
    return render_template("index.html", tasks=tasks)
 

if __name__ == "__main__":
    init_db()
    app.run(debug=True)