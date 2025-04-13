### Create a Book

 from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

### Retrieve a Book 
books = Book.objects.all()
books
book = Book.objects.get(title="1984")
book.title
book.author
book.publication_year

### Update a Book 
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book

### Delete a Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()