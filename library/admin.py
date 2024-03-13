from django.contrib import admin
from .models import Book, IjaraKitob, Student
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'count')
    list_display_links = ['id', 'title', 'description', 'price', 'count']
    ordering = ('title',)
    search_fields = ['title', 'description',]
    filter = ['title']


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'role')
    search_fields = ['first_name', 'last_name', 'role']


@admin.register(IjaraKitob)
class IjaraKitobAdmin(ImportExportModelAdmin):
    list_display = ('id', 'student', 'book', 'returned_date', 'created_date')
    # autocomplete_fields = ['Student', 'book']
    search_fields = ['student', 'book']
    # filter = ['Student', 'book']

