from abc import ABC, abstractmethod
from app.core.exceptions import BorrowLimitExceededError


class Member(ABC):
    def __init__(self, member_id: int, name: str):
        self._member_id = member_id
        self._name = name
        self._borrowed_books = []

    @property
    def member_id(self):
        return self._member_id

    def borrow_book(self, book):
        if len(self._borrowed_books) >= self.borrow_limit:
            raise BorrowLimitExceededError("Borrow limit exceeded")
        self._borrowed_books.append(book)

    def return_book(self, book):
        self._borrowed_books.remove(book)

    @property
    @abstractmethod
    def borrow_limit(self):
        pass

    def __str__(self):
        return f"[{self.member_id}] {self._name} | Borrowed: {len(self._borrowed_books)}/{self.borrow_limit}"
