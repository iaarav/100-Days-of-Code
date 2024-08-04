from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///newBooksCollection.db"
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.execute(db.select(Books).order_by(Books.id)).scalars().all()

    print(all_books)

    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            db.session.add(
                Books(
                    title=request.form["title"],
                    author=request.form["author"],
                    rating=request.form["rating"]

                )
            )
            db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/editRating', methods=["GET", "POST"])
def edit():
    id = request.args.get('id')

    if request.method == "POST":
        db.get_or_404(Books, id).rating = float(request.form["rating"])
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('edit.html', book=db.get_or_404(Books, id))


@app.route('/deleteBook')
def deleteBook():
    id = request.args.get('id')

    db.session.delete(db.get_or_404(Books, id))
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
