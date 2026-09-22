from app import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer,primary_key=True)

    title = db.Column(db.String(150),nullable=False)

    author = db.Column(db.String(120),nullable=False)

    price = db.Column(db.Float,nullable=False)

    published_year = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'published_year': self.published_year
        }