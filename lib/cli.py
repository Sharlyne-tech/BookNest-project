from lib.helpers import view_all_books, search_books_by_title, borrow_book, return_book, delete_book
from lib.seeds import seed_data

# Preload books
books = seed_data()

def menu():
    while True:
        print("\n📚 Welcome to BookNest 📚")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Delete a book")
        print("6. Exit")

        choice = input("Enter your choice (1–6): ").strip()
        print(f"You entered: '{choice}'")  # Debug line

        if choice == "1":
            view_all_books(books)
        elif choice == "2":
            title = input("Enter book title: ")
            matches = search_books_by_title(books, title)
            if matches:
                for book in matches:
                    print(f"{book.title} by {book.author.name}")
            else:
                print("No books found.")
        elif choice == "3":
            borrow_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            delete_book(books)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the menu
menu()