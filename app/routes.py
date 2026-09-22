from flask import jsonify,request

from app import app,csrf,auth
from app.models import Book,db


# @app.route('/books')
# def get_books():
#     books = Book.query.all()
#     # books_list = []
#     # for book in books:
#     #     books_list.append(book.to_dict())
#     books_list = [book.to_dict() for book in books]
#     return jsonify(books_list)
@app.route('/books')
@auth.login_required
def get_books():
    author = request.args.get("author")
    if author:
        books = Book.query.filter_by(author=author).all()
    else:
        books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/books/<int:id>')
def get_book(id):
    book = db.session.get(Book,id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book.to_dict()),200

@csrf.exempt
@app.route('/books', methods=['POST'])
def create_book():
    if not request.is_json:
        return jsonify({'error':'Request must be jason'}),415

    data = request.get_json()

    title = data.get('title')
    author = data.get('author')
    price = data.get('price')
    published_year = data.get('published_year')
    if not title or not author or not price or not published_year:
        return jsonify({'error':'All field are requerd '}),400
    
    book = Book(
        title=title,
        author=author,
        price=price,
        published_year=published_year
        )
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()),201

@csrf.exempt
@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 415
    
    book = db.session.get(Book, id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    price = data.get('price')
    published_year = data.get('published_year')

    if not title or not author or not price or not published_year:
        return jsonify({'error':'All field are requerd '}),400
    book.title = title
    book.author = author
    book.price = price
    book.published_year = published_year
    db.session.commit()
    return jsonify(book.to_dict()), 200

@csrf.exempt
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = db.session.get(Book,id)
    if not book:
        return jsonify({'error':'Book not found'}),404
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"}),200

@auth.verify_password
def verify_password(username, password):
    if username == "admin" and password == "1234":
        return username

    return None


    
    