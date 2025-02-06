# Aggregation represents a relationship where one object (the whole) 
# contains references to one or more independent objects (the parts).
# In this case, a Library contains Book objects, but the Book objects 
# can exist independently of the Library. 
# This means that the life cycle of the books does not depend on the library.

class Library:
    """Represents a library that holds a collection of books."""
    
    def __init__(self, name):
        """Initialize the library with a name and an empty list of books."""
        self.name = name
        self.books = []  # The books list will store instances of the Book class.

    def add_book(self, book):
        """Add a book to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """List the books in the library with their title and author."""
        return [f'{book.title} by {book.author}' for book in self.books]


class Book:
    """Represents a book with a title and author."""
    
    def __init__(self, title, author):
        """Initialize the book with a title and author."""
        self.title = title
        self.author = author


# Create a library instance
library = Library('New York Public Library')

# Create book instances
book1 = Book('Harry Potter...', 'J. K. Rowling')
book2 = Book('The Hobbit', 'J. R. R. Tolkien')
book3 = Book('The Colour of Magic', 'Terry Pratchett')

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)  # Output: New York Public Library

# Print list of books in the library
# This will print each book's title and author using the list_books method.
for book in library.list_books():
    print(book)
    # Output:
    # Harry Potter... by J. K. Rowling
    # The Hobbit by J. R. R. Tolkien
    # The Colour of Magic by Terry Pratchett
