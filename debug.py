from lib.models import Author, Book
from lib.helpers import view_all_books


author = Author(name="Test Author")
book = Book(title="Debug Book", author=author)


print("Author created:", author.name)
print("Book created:", book.title)

view_all_books()