from . import con, cur

def test():
    return "sqlite connect ok"


def borrow(borrower, book_id):
    sql = "insert into borrowings(borrower, book_id) values (?, ?)"
    cur.execute(sql, (borrower, book_id))
    con.commit()
    return True

def set_borrow_time(borrower, book_id):
    sql = "update borrowings set borrowed_at = current_timestamp where borrower = ? and book_id = ?"
    cur.execute(sql, (borrower, book_id))
    con.commit()
    return True

def get_borrows_by_borrower(borrower):
    sql = "select book_id from borrowings where borrower = ?"
    cur.execute(sql, borrower)
    return cur.fetchall()

def get_borrows_by_borrower_and_book_id(borrower, book_id):
    sql = "select * from borrowings where borrower = ? and book_id = ?"
    cur.execute(sql, (borrower, book_id, ))
    return cur.fetchone()


def return_borrow(borrower, book_id):
    sql = "update borrowings set returned_at=current_timestamp where borrower = ? and book_id = ?"
    cur.execute(sql, (borrower, book_id))
    con.commit()
    return True


def get_borrows_by_month(borrow_month):
    sql = "select borrower, title, author from borrowings join books on borrowings.book_id = books.book_id where strftime('%m', borrowed_at) = ?"
    cur.execute(sql, (borrow_month, ))
    return cur.fetchall()