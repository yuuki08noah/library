from fastapi import APIRouter, Body

from model.borrowings import ReturnRequest
from service import borrowings as service

router = APIRouter()

@router.post("/return")
def retrn(body: ReturnRequest = Body(...)):
    return service.return_borrow(body)