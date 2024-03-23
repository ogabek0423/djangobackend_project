from django.contrib import admin
from .models import Book, BookRecord, Customers, CoursesRecord, CourseSpeciality, Teacher

admin.site.register(Book)
admin.site.register(BookRecord)
admin.site.register(Customers)
admin.site.register(CoursesRecord)
admin.site.register(CourseSpeciality)
admin.site.register(Teacher)
