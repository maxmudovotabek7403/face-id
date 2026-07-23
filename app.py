from flask import Flask, render_template
from datetime import datetime

from models import db, Student

app = Flask(__name__)

app.config["SECRET_KEY"] = "smartface_ai_2026"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def dashboard():

    total_students = Student.query.count()

    return render_template(
        "dashboard.html",
        total_students=total_students,
        today_attendance=18,
        unknown_faces=2,
        camera_status="Online",
        current_time=datetime.now().strftime("%d.%m.%Y %H:%M")
    )


@app.route("/students")
def students():

    students = Student.query.all()

    return render_template(
        "students.html",
        students=students
    )


@app.route("/camera")
def camera():

    return render_template("camera.html")


if __name__ == "__main__":
    app.run(debug=True)