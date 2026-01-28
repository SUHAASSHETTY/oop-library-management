from app.core.enums import BookStatus
from app.core.exceptions import BookNotAvailableError


class Book:
    def __init__(self, book_id: int, title: str, author: str):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._status = BookStatus.AVAILABLE

    @property
    def book_id(self):
        return self._book_id

    def issue(self):
        if self._status == BookStatus.ISSUED:
            raise BookNotAvailableError("Book already issued")
        self._status = BookStatus.ISSUED

    def return_book(self):
        self._status = BookStatus.AVAILABLE

    def __str__(self):
        return f"[{self.book_id}] {self._title} by {self._author} ({self._status.value})"
