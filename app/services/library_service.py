from app.core.exceptions import LibraryError
from app.models.book import Book
from app.models.member import Member


class LibraryService:
    def __init__(self):
        self._books = {}
        self._members = {}

    def add_book(self, book: Book):
        self._books[book.book_id] = book

    def add_member(self, member: Member):
        self._members[member.member_id] = member

    def issue_book(self, book_id: int, member_id: int):
        try:
            book = self._books[book_id]
            member = self._members[member_id]

            book.issue()
            member.borrow_book(book)

            print(f" Book issued to {member}")

        except KeyError:
            print("Invalid Book or Member ID")
        except LibraryError as e:
            print(f" {e}")

    def return_book(self, book_id: int, member_id: int):
        try:
            book = self._books[book_id]
            member = self._members[member_id]

            if book not in member._borrowed_books:
                raise LibraryError("Invalid return")

            book.return_book()
            member.return_book(book)

            print("Book returned")

        except KeyError:
            print("Invalid Book or Member ID")
        except LibraryError as e:
            print(f" {e}")

    def show_books(self):
        for book in self._books.values():
            print(book)

    def show_members(self):
        for member in self._members.values():
            print(member)
