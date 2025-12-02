from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from django.views.generic import TemplateView, DetailView, UpdateView


# Create your views here.
# Function based views
def hello_view(request):
    return HttpResponse("Hello!")

def book_list(request):
    books = Book.objects.all()
    context = {'book_list':books}
    return render(request, 'book_list.html', context)

# Class based views 
class HelloView(TemplateView):
    template_name = 'hello.html'
    
# class BookDetailView(DetailView):
#     model = Book 
#     template_name = 'books/book_detail.html'
#     def get_context_data(self, **kwargs):
#         book = self.get_object()
#         context['average_rating'] = book.get_average_rating()