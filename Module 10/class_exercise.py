class Author:
    def __init__(self, name, books):
        self.name = name
        self.books = []

    def set_book(self, title):
        self.books.append(title)



class Book:
    def __init__(self, title):
        self.title = title
        self.books = []


a = Author("J.K. Rowling")
a1 = Book("Harry Potter 1")
a2 = Book("Harry Potter 2")
a.set__book(a1)
a.set_book(a2)
b = Author("George Orwell")
b1 = Book("1984")
b2 = Book("?")
b.add_book(b1)
b.add_book(b2)

print(f"Author: {a.name}")
for book in a.books:
          print(f"- {book.title}")

print(f"\nAuthor: {b.name}")
for book in b.books:
    print(f"- {book.title}")
