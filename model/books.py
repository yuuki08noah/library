from pydantic import BaseModel


class BookRequest(BaseModel):
    title: str
    author: str

class BookResponse(BaseModel):
    title: str
    author: str