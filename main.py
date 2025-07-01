import sqlite3

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from exception.book import BookException
from web import borrowings as borrow_web
from web import books as books_web
from web import retrn as return_web

app = FastAPI()
app.include_router(borrow_web.router)
app.include_router(books_web.router)
app.include_router(return_web.router)

@app.exception_handler(BookException)
def book_exception_handler(request: Request, exc: BookException):
    return JSONResponse(status_code=400, content=False)

@app.exception_handler(sqlite3.IntegrityError)
def sqlite_exception_handler(request: Request, exc: sqlite3.IntegrityError):
    print(exc.args[0])
    return JSONResponse(status_code=400, content=False)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', reload=True)
