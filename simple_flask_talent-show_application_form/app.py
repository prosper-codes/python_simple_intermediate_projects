from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(100))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        date_str = request.form.get("date")
        occupation = request.form.get("occupation")

        date = datetime.strptime(date_str, "%Y-%m-%d").date()

        form = Form(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date=date,
            occupation=occupation
        )

        db.session.add(form)
        db.session.commit()

        print("Data saved successfully!")

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)