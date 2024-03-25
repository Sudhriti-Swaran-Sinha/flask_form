from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///form_data.db"
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date_c: Mapped[int] = mapped_column(Integer, nullable=False)
    name_c: Mapped[String] = mapped_column(String(250), unique=True, nullable=False)
    phone_c: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    feedback_c: Mapped[String] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        date = request.form['date']
        name = request.form['name']
        phone = request.form['number']
        feedback = request.form['feedback']

        with app.app_context():
            newbook = Book(date_c=date, name_c=name, phone_c=phone, feedback_c=feedback)
            db.session.add(newbook)
            db.session.commit()



    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
