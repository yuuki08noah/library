from data import borrowings as data
from cache import borrower as cache

def test():
    db_test = data.test()
    redis_test = cache.test()
    return {"sqlite": db_test, "redis": redis_test}