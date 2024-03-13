from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField(default=1)
    count = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)


class Student(models.Model):
    ROLE = (
        ('Student', 'Student'),
        ('Manager', 'Manager'))

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=ROLE, default='Student')


class IjaraKitob(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    returned_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_created=True)



