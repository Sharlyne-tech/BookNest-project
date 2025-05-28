from lib.models import Book, Author
def view_all_books(books):
    for book in books:
        status = "Borrowed" if book.borrowed else "Available"
        print(f"{book.title} by {book.author.name} - {status}")

def search_books_by_title(books, title):
    return [book for book in books if title.lower() in book.title.lower()]

def borrow_book(books):
    title = input("Enter the title of the book to borrow: ")
    for book in books:
        if book.title.lower() == title.lower():
            if book.borrowed:
                print("That book is already borrowed.")
            else:
                book.borrowed = True
                print(f"You have borrowed '{book.title}'")
            return
    print("Book not found.")

def return_book(books):
    title = input("Enter the title of the book to return: ")
    for book in books:
        if book.title.lower() == title.lower():
            if not book.borrowed:
                print("That book wasn’t borrowed.")
            else:
                book.borrowed = False
                print(f"You have returned '{book.title}'")
            return
    print("Book not found.")

def delete_book(books):
    title = input("Enter the title of the book to delete: ")
    for book in books:
        if book.title.lower() == title.lower():
            books.remove(book)
            print(f"'{book.title}' has been deleted.")
            return
    print("Book not found.")

def add_book(author, books, book):
    books.append(book)