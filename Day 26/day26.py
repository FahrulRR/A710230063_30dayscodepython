# Definisikan kelas Book
class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

# Definisikan kelas Member
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

# Definisikan kelas Library
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_id, ISBN):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.ISBN == ISBN), None)
        
        if member and book:
            return member.borrow_book(book)
        return False

    def return_book(self, member_id, ISBN):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.ISBN == ISBN), None)

        if member and book:
            return member.return_book(book)
        return False

# Contoh penggunaan
library = Library()

# Tambahkan buku
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321")
library.add_book(book1)
library.add_book(book2)

# Tambahkan member
member1 = Member("Alice", 1)
member2 = Member("Bob", 2)
library.add_member(member1)
library.add_member(member2)

# Pinjam buku
print(library.borrow_book(1, "123456789"))  # Output: True
print(library.borrow_book(2, "123456789"))  # Output: False

# Kembalikan buku
print(library.return_book(1, "123456789"))  # Output: True
print(library.borrow_book(2, "123456789"))  # Output: True
