from flask import Flask, render_template, request, redirect
import json, random

app = Flask(__name__)

def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    data = load_data()
    quote = random.choice(data["quotes"]) if data["quotes"] else "Have a great day!"
    grades = data["grades"]
    avg = round(sum([g["grade"] for g in grades]) / len(grades), 2) if grades else 0
    return render_template("index.html", tasks=data["tasks"], notes=data["notes"],
        timetable=data["timetable"], grades=grades, average=avg, quote=quote,
        reminders=data.get("reminders", []))

@app.route("/add_task", methods=["POST"])
def add_task():
    data = load_data()
    task = request.form["task"]
    due = request.form["due"]
    data["tasks"].append({"task": task, "due": due})
    save_data(data)
    return redirect("/")

@app.route("/delete_task/<int:index>")
def delete_task(index):
    data = load_data()
    data["tasks"].pop(index)
    save_data(data)
    return redirect("/")

@app.route("/add_note", methods=["POST"])
def add_note():
    data = load_data()
    note = request.form["note"]
    data["notes"].append(note)
    save_data(data)
    return redirect("/")

@app.route("/delete_note/<int:index>")
def delete_note(index):
    data = load_data()
    data["notes"].pop(index)
    save_data(data)
    return redirect("/")

@app.route("/add_slot", methods=["POST"])
def add_slot():
    data = load_data()
    day = request.form["day"]
    time = request.form["time"]
    subject = request.form["subject"]
    if day not in data["timetable"]:
        data["timetable"][day] = []
    data["timetable"][day].append({"time": time, "subject": subject})
    save_data(data)
    return redirect("/")

@app.route("/add_grade", methods=["POST"])
def add_grade():
    data = load_data()
    subject = request.form["subject"]
    grade = float(request.form["grade"])
    data["grades"].append({"subject": subject, "grade": grade})
    save_data(data)
    return redirect("/")

@app.route("/add_reminder", methods=["POST"])
def add_reminder():
    data = load_data()
    message = request.form["message"]
    time = request.form["time"]
    data["reminders"].append({"message": message, "time": time})
    save_data(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)