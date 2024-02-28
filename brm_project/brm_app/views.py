from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def hello_world(request):
    return render(request, "view_book.html")


def add_book_view(request):
    # if request.method=="POST":
    #     title = request.POST["title"]
    #     price = request.POST["price"]
    #
    #     Book = Book()
    #
    #     book.title = title
    #     book.price = price
    #     book.save()
   return render(request, "add_book.html")


def add_book(request):
    if request.method=="POST":
        title = request.POST["title"]
        price = request.POST["price"]

        Book = Book()

        book.title = title
        book.price = price
        book.save()
        return HttpResponse('/add_book')