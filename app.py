from flask import Flask, render_template, request

app = Flask(__name__)


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
    return render_template("index.html", task1=task1, task2=task2, task3=task3)
 

if __name__ == "__main__":
    app.run(debug=True)