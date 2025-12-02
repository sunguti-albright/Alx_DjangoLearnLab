from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, SignUpView


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", TemplateView.as_view(template_name="accounts/profile.html"), name="profile",),
    path("signup/", SignUpView.as_view(), name="templates/registration/signup"),
    path("hello/", views.hello_view, name="hello"),
    path("books_list/", views.book_list, name="books"),
    # path('about/', views.AboutView.as_view(), name='about'), # type: ignore
]
