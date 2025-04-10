from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

# Create your views here.
def hello_view(request):
    return HttpResponse("Hello!")


def book_list(request):
    books = Book.objects.all()
    context = {'book_list':books}
    return render(request, 'books/book_list.html', context)
