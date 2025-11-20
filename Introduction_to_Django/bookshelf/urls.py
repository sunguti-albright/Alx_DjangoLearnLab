from django.urls import path
from . import views 

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('books_list/', views.book_list, name='books'),
    # path('about/', views.AboutView.as_view(), name='about'), # type: ignore
]