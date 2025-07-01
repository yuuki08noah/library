from datetime import datetime

from data import borrowings as data
from data import books as book_data
from cache import borrower as cache
from exception.book import BookNotAvailable
from model.borrowings import BorrowRequest, BorrowResponse, BorrowMonthResponse


def test():
    db_test = data.test()
    redis_test = cache.test()
    return {"sqlite": db_test, "redis": redis_test}


def borrow(body: BorrowRequest):
    book = book_data.get_book_by_title(body.title)
    if not book or book[-1] == 0: # 해당 책이 없거나 Not Available 할때
        raise BookNotAvailable()
    book_id = book[0]
    borrow = data.get_borrows_by_borrower_and_book_id(body.borrower, book_id) # 예전에 해당 도서를 해당 대출자가 대출한 적이 있다면 시간만 바꿔줌
    return (data.borrow(body.borrower, book_id) if not borrow else data.set_borrow_time(body.borrower, book_id) and
            cache.borrow(body.borrower, body.title) and
            book_data.toggle_book_available_by_book_id(book_id, 0))

def get_borrows_by_borrower(borrower):
    return BorrowResponse(borrower=borrower, books=cache.get_borrows_by_borrower(borrower))

def return_borrow(body):
    book = book_data.get_book_by_title(body.title)

    book_id = book[0]
    return (data.return_borrow(body.borrower, book_id) and
            cache.return_borrow(body.borrower, body.title) and
            book_data.toggle_book_available_by_book_id(book_id, 1))

def row_to_model(row):
    return BorrowMonthResponse(borrower=row[0], title=row[1], author=row[2])

def get_borrows_by_month(borrow_month):
    if borrow_month < 10:
        borrow_month = "0" + str(borrow_month)
    return list(map(row_to_model, data.get_borrows_by_month(borrow_month)))