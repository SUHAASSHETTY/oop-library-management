# 📚 Library Management System – Python (OOP)

A **console-based Library Management System** built using **Python** to demonstrate **advanced Object-Oriented Programming (OOP)** concepts and **industry-style project structuring**.

This project is not just a basic OOP example — it follows **clean architecture**, **separation of concerns**, and **scalable design principles** commonly used in real-world backend systems.

---

## Project Overview

Managing a library involves handling:
- Books and their availability
- Different types of members
- Borrowing and returning rules
- Validation and error handling

This system models all of the above using **Python OOP principles**, making the code:
- Easy to read
- Easy to maintain
- Easy to extend (database, API, UI, etc.)

---

## Key Features

- Add and manage library books
- Support for multiple member types
  - Students
  - Faculty
- Role-based borrowing limits
- Issue and return books with validation
- Custom exception handling for clean error flow
- Modular, layered project architecture
- Demonstrates real-world OOP usage (not toy examples)

---

## Project Architecture

The project follows a **layered architecture** approach:

```
library-management-system/
│
├── app/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── enums.py              # Enums (Book status)
│   │   └── exceptions.py         # Custom domain exceptions
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── book.py               # Book entity
│   │   ├── member.py             # Abstract Member base class
│   │   ├── student.py            # Student member (inherits Member)
│   │   └── faculty.py            # Faculty member (inherits Member)
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── library_service.py   # Core business logic
│   │
│   └── ui/
│       ├── __init__.py
│       └── menu.py               # Command-line menu handling
│
├── main.py                       # Application entry point
├── requirements.txt
├── .gitignore
└── README.md
```

### Why This Structure?

- **Models** → represent real-world entities  
- **Services** → contain business rules  
- **UI** → handles user interaction  
- **Core** → shared enums & exceptions  

This mirrors how **production-grade Python applications** are structured.

---

## OOP Concepts Demonstrated

### 1️⃣ Encapsulation
- Private attributes (`_attribute`)
- Controlled access using properties

### 2️⃣ Abstraction
- `Member` is an **abstract base class**
- Forces all member types to follow a common contract

### 3️⃣ Inheritance
- `Student` and `Faculty` inherit from `Member`

### 4️⃣ Polymorphism
- Different borrowing limits for different member types
- Same method behaves differently based on object type

### 5️⃣ Enums
- `BookStatus` enum replaces primitive booleans
- Improves readability and safety

### 6️⃣ Custom Exceptions
- Domain-specific errors like:
  - Book already issued
  - Borrow limit exceeded
- Keeps business logic clean and readable

---

## How to Run the Project

### Prerequisites
- Python **3.8 or above**
- No external libraries required

### Clone the Repository
```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

### Run the Application
```bash
python main.py
```

---

## Sample Output

```
--- Library Menu ---
1. Show Books
2. Show Members
3. Issue Book
4. Return Book
5. Exit
Enter choice: 1

[1] Python Basics by Guido (Available)
[2] Advanced OOP by James (Available)

--- Library Menu ---
1. Show Books
2. Show Members
3. Issue Book
4. Return Book
5. Exit
Enter choice: 3
Book ID: 1
Member ID: 101
Book issued to [101] Alice | Borrowed: 1/2

--- Library Menu ---
1. Show Books
2. Show Members
3. Issue Book
4. Return Book
5. Exit
Enter choice: 3
Book ID: 2
Member ID: 101
Book issued to [101] Alice | Borrowed: 2/2

--- Library Menu ---
1. Show Books
2. Show Members
3. Issue Book
4. Return Book
5. Exit
Enter choice: 3
Book ID: 1
Member ID: 101
Borrow limit exceeded
```

---

## Error Handling Examples

The system handles various error scenarios gracefully:

- Issuing an already issued book
- Returning a book not borrowed by the member
- Exceeding borrowing limits
- Invalid book or member IDs

All errors are handled using **custom exceptions**, not messy if-else chains.

---

## Learning Outcomes

By studying or building this project, you will understand:

How OOP works in real-world systems  
How to structure Python projects professionally  
How business logic differs from UI logic  
How to design code that scales beyond a single file  
The importance of separation of concerns  
How to use abstract base classes effectively  
How to implement custom exception handling  

---

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## Author

**Suhaas S**  

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute it.

---

## Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!

---

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [SOLID Principles](https://realpython.com/solid-principles-python/)

---

**Made with ❤️ and Python**
