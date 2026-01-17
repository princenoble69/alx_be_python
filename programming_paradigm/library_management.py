class Book:
    """Represents a book with a title, author, and availability status."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books."""
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and checks it out."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return
        print(f"Book '{title}' is not available or doesn't exist.")

    def return_book(self, title):
        """Finds a book by title and returns it."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        """Prints all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
