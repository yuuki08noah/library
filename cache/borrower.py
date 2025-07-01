from . import redis_client

def test():
    return "redis connect ok"


def borrow(borrower, title):
    borrow_key = f"borrower:{borrower}:books"
    redis_client.sadd(borrow_key, title)
    return True

def get_borrows_by_borrower(borrower):
    borrow_key = f"borrower:{borrower}:books"
    return redis_client.smembers(borrow_key)

def return_borrow(borrower, title):
    borrow_key = f"borrower:{borrower}:books"
    return bool(redis_client.srem(borrow_key, title))