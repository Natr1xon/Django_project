from tkinter.constants import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

Author = get_user_model()

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    genre = models.CharField(max_length=256, verbose_name="Жанр")
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор",blank=True)

    def __str__(self):
        return self.title

class Reader(models.Model):
    firstname = models.CharField(max_length=256, verbose_name="Имя")
    lastname = models.CharField(max_length=256, verbose_name="Фамилия")
    date_of_birth = models.DateTimeField(verbose_name="Дата рождения")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Borrow(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name="Читатель",blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга",blank=True)
    borrow_date = models.DateTimeField(verbose_name="Дата выдачи",default=timezone.now)
    return_date = models.DateTimeField(verbose_name="Дата возврата",null = True, blank = True)

    def __str__(self):
        return f"{self.reader} - {self.book}"
