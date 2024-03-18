from django.contrib import admin
from .models import Book, BookRecord, Customers

admin.site.register(Book)
admin.site.register(BookRecord)
admin.site.register(Customers)

