from django.urls import path, include, re_path
from .views import hello_world, add_book_view, add_book
urlpatterns = [
    path("", hello_world),
    path("add_book/", add_book_view),
    path("/add_book/add_book/", add_book)
]