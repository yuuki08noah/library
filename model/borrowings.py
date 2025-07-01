from typing import List

from pydantic import BaseModel


class BorrowRequest(BaseModel):
    borrower: str
    title: str

class ReturnRequest(BaseModel):
    borrower: str
    title: str

class BorrowResponse(BaseModel):
    borrower: str
    books: List[str]

class BorrowMonthResponse(BaseModel):
    borrower: str
    title: str
    author: str