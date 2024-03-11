from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Book


class BookListView(View):
    def get(self, request):
        search =request.GET.get('search')
        if not search:
            books = Book.objects.all()
            context = {'books': books}
            return render(request, 'library/book.html', context)
        else:
            books = Book.objects.filter(title__icontains=search)
            context = {'books': books}
            return render(request, 'library/book.html', context)



class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        context = {'book': book}
        return render(request, 'library/book_detail.html', context)

