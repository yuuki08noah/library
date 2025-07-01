from starlette import status


class BookException(Exception):
    def __init__(self, message, status_code: int = status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class BookNotAvailable(BookException):
    def __init__(self):
        super().__init__(
            message=f"Book is not available",
        )
