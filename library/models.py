from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField()

    def __str__(self):
        return f"{self.title},{self.description},{self.price},{self.count}\n"


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    group_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.group_name}"


class Booking_book(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    talked_date = models.DateTimeField()

    def __str__(self):
        return f"{self.book_id},{self.student_id},{self.talked_date}"




