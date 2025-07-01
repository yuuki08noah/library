from data import cur, con


def save(title, author):
    sql = "insert into books (title, author) values (?, ?)"
    cur.execute(sql, (title, author))
    con.commit()
    return True

def get_available_books():
    sql = "select title, author from books where available = 1"
    cur.execute(sql)
    return cur.fetchall()

def get_book_by_title(title):
    sql = "select * from books where title = ?"
    cur.execute(sql, (title,))
    return cur.fetchone()

def delete_book_available_by_book_id(book_id):
    sql = "delete from books where book_id = ?"
    cur.execute(sql, (book_id,))
    con.commit()
    return True

def toggle_book_available_by_book_id(book_id, available):
    sql = "update books set available = available where book_id = ?"
    cur.execute(sql, (book_id,))
    con.commit()
    return True

def get_book_by_book_id(book_id):
    sql = "select * from books where book_id = ?"
    cur.execute(sql, (book_id,))
    return cur.fetchone()