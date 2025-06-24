from fastapi import APIRouter
from service import borrowings as service

router = APIRouter(prefix="/borrows")

@router.get("")
def test():
    return service.test()