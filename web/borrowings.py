from fastapi import APIRouter, Body

from model.borrowings import BorrowRequest
from service import borrowings as service

router = APIRouter(prefix="/borrows")

@router.get("")
def test():
    return service.test()

@router.post("")
def borrow(body: BorrowRequest = Body(...)):
    return service.borrow(body)


@router.get("/month/{borrow_month}")
def get_borrows_by_month(borrow_month: int):
    return service.get_borrows_by_month(borrow_month)

@router.get("/{borrower}/books")
def get_borrows_by_borrower(borrower: str):
    return service.get_borrows_by_borrower(borrower)