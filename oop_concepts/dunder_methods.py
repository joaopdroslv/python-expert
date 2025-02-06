# The Book class represents a book with title, author, and number of pages.
# It includes several special methods to enable various functionalities 
# like comparison, addition, and key-based access.

class Book:
    def __init__(self, title, author, num_pages):
        """Initialize the book with title, author, and number of pages."""
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        """Return a string representation of the book, showing the title and author."""
        return f'"{self.title}" by {self.author}'

    def __eq__(self, other):  
        """Check if two books are equal based on their title and author."""
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        """Compare the number of pages between two books."""
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        """Compare the number of pages between two books."""
        return self.num_pages > other.num_pages

    def __add__(self, other):
        """Add the number of pages of two books and return the sum."""
        return f'{self.num_pages + other.num_pages} pages'

    def __contains__(self, keyword):
        """Check if the keyword is found in either the title or author."""
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        """Access the book's attributes like 'title', 'author', and 'num_pages' using a key."""
        attributes = {
            'title'     : self.title,
            'author'    : self.author,
            'num_pages' : self.num_pages
        }
        return attributes.get(key, f'Key "{key}" was not found.')


# Testing the Book class with various operations

book1 = Book('The Hobbit', 'J.R.R. Tolkien', 310)  
book2 = Book("Harry Potter and The Philosopher's Stone", 'J.K. Rowling', 223)
book3 = Book('The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 172)

# __str__ method: Printing the book's title and author
print(book1)  # Expected output: "The Hobbit" by J.R.R. Tolkien

# __eq__ method: Comparing if two books are equal
print(book1 == book2)  # Expected output: False (Different titles and authors)

# __lt__ method: Checking if book1 has fewer pages than book2
print(book1 < book2)  # Expected output: False (310 pages is not less than 223 pages)

# __gt__ method: Checking if book1 has more pages than book2
print(book1 > book2)  # Expected output: True (310 pages is more than 223 pages)

# __add__ method: Adding the number of pages from book1 and book2
print(book1 + book2)  # Expected output: '533 pages'

# __contains__ method: Checking if a keyword is in the title or author of the book
print('Lion' in book3)  # Expected output: True (The title contains 'Lion')
print('Lion' in book2)  # Expected output: False (The title doesn't contain 'Lion')
print('Rowling' in book1)  # Expected output: False (The author is not 'Rowling')

# __getitem__ method: Accessing attributes of the book by key
print(book1['title'])  # Expected output: 'The Hobbit'
print(book1['author'])  # Expected output: 'J.R.R. Tolkien'
print(book1['num_pages'])  # Expected output: 310
print(book1['x'])  # Expected output: 'Key "x" was not found.'
