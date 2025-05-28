from lib.models import  Author, Book
from lib.helpers import add_book

def seed_data():
    authors = []
    books = []

    a1 = Author(1, "Chinua Achebe", "Nigerian novelist")
    a2 = Author(2, "J.K. Rowling", "British author")
    a3 = Author(3, "George Orwell", "English novelist and critic")
    a4 = Author(4, "Jane Austen", "Classic English novelist")

    b1 = Book(1, "Things Fall Apart", "Historical", a1)
    b2 = Book(2, "Harry Potter", "Fantasy", a2)
    b3 = Book(3, "1984", "Dystopian", a3)
    b4 = Book(4, "Pride and Prejudice", "Romance", a4)
    b5 = Book(5, "Animal Farm", "Satire", a3)

    add_book(a1, books, b1)
    add_book(a2, books, b2)
    add_book(a3, books, b3)
    add_book(a4, books, b4)
    add_book(a3, books, b5)

    authors.extend([a1, a2, a3, a4])
    return authors, books