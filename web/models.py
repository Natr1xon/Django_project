from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth import get_user_model

Author = get_user_model()

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    author_id = models.ForeignKey(Author, on_delete = models.CASCADE)

class Reader(models.Model):
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    date_of_birth = models.DateTimeField()

class Borrow(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)