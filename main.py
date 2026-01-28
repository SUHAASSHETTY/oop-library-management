from app.services.library_service import LibraryService
from app.models.book import Book
from app.models.student import Student
from app.models.faculty import Faculty
from app.ui.menu import show_menu


def main():
    library = LibraryService()

    library.add_book(Book(1, "Python Basics", "Guido"))
    library.add_book(Book(2, "Advanced OOP", "James"))

    library.add_member(Student(101, "Alice"))
    library.add_member(Faculty(201, "Dr. Bob"))

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            library.show_books()
        elif choice == "2":
            library.show_members()
        elif choice == "3":
            library.issue_book(int(input("Book ID: ")), int(input("Member ID: ")))
        elif choice == "4":
            library.return_book(int(input("Book ID: ")), int(input("Member ID: ")))
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
