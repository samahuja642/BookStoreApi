from store_app import app
from store_app.models import Book
from flask import jsonify,request

@app.route('/books/createBook',methods=["POST"])
def newbook():
    if request.headers.get('Content-Type') == 'application/json':
        try:
            object_data = request.get_json()
            book1 = Book(**object_data).save()
            return "",201
        except:
            return "JSON not valid",400
    return "content type should be json",400

@app.route('/books',methods=["GET"])
def getbooks():
    books = Book.objects()
    return jsonify(books),200

@app.route('/books/update/<int:id>/',methods=["PUT"])
def update_book(id):
    if request.headers.get('Content-Type') == 'application/json':
        try:
            object_data = request.get_json()
            book_object = Book.objects.get_or_404(book_id=id)
            book_object.update(**object_data)
            return "",201
        except:
            return "JSON not valid",400
    return "content type should be json",400

@app.route('/books/delete/<int:id>/',methods=["DELETE"])
def delete_book(id):
    book_object = Book.objects.get_or_404(book_id=id)
    book_object.delete()
    return jsonify(book_object),200

    
    
