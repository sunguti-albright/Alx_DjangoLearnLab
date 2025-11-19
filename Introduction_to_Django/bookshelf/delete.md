### Delete the book

from bookshelf.models import Book
book = Book.objects.first()
book.delete()
Book.objects.all()