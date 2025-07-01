from exception.book import BookNotAvailable
from model.books import BookRequest, BookResponse
from data import books as data

def row_to_model(row):
    return BookResponse(title=row[0], author=row[1])

def post_book(body: BookRequest):
    return data.save(body.title, body.author)

def get_available_books():
    return list(map(row_to_model, data.get_available_books()))

def delete_book_available_by_book_id(book_id):
    book = data.get_book_by_book_id(book_id)
    if not book or not book[-1]:
        raise BookNotAvailable()
    return data.delete_book_available_by_book_id(book_id)