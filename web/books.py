from fastapi import APIRouter, Body

from model.books import BookRequest
import service.books as service

router = APIRouter(prefix="/books")

@router.post("")
def post_book(body: BookRequest = Body(...)):
    return service.post_book(body) or False

@router.get("")
def get_available_books():
    return service.get_available_books()

@router.delete("/{book_id}")
def delete_book_available_by_book_id(book_id: int):
    return service.delete_book_available_by_book_id(book_id) or False