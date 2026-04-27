from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-book-collection.db'
db.init_app(app)


class NewBook(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'Book {self.title}'


with app.app_context():
    db.create_all()

# # Create new record
# with app.app_context():
#     new_book = NewBook(title='ACATAR 2', author='Sara J. Maas', rating=7.8)
#     db.session.add(new_book)
#     db.session.commit()


# Read All records
with app.app_context():
    result = db.session.execute(db.select(NewBook).order_by(NewBook.title))
    all_books = result.scalars()

# Update a record
# with app.app_context():
#     book_to_update = db.session.execute(db.select(NewBook).where(NewBook.title == "ACATAR 2")).scalar()
#     book_to_update.rating = 8.0
#     db.session.commit()


# Update record by primery key
# book_id = 2
# with app.app_context():
#     book_to_update = db.session.execute(db.select(NewBook).where(NewBook.id == book_id)).scalar()
#     book_to_update.rating = 6.5
#     db.session.commit()


# Delete a book by primery key
book_id = 2
with app.app_context():
    book_to_delete = db.session.execute(db.select(NewBook).where(NewBook.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
