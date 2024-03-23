from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Book, CoursesRecord, CourseSpeciality, Teacher
from django.contrib.auth.mixins import LoginRequiredMixin

class BookListView(LoginRequiredMixin, View):
    def get(self, request):
        search =request.GET.get('search')
        if not search:
            books = Book.objects.all()
            context = {'books': books}
            return render(request, 'library/book.html', context)
        else:
            book = Book.objects.filter(title__icontains=search)
            if not book:
                return HttpResponse('<h1>No book found</h1>')
            else:
                context = {'books': book,
                           'search': search}
                return render(request, 'library/book.html', context)

        books = Book.objects.all()
        return render(request, 'library/book.html', {'books': books})


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        context = {'book': book}
        return render(request, 'library/book_detail.html', context)


class CourseListView(View):
    def get(self, request):
        context = {'courses': CoursesRecord.objects.all()}
        return render(request, 'courses.html', context)


class TeacherList(View):
    def get(self, request):
        context = {'teachers': Teacher.objects.all()}
        return render(request, 'teacher.html', context)

