from django.contrib import admin
from django.urls import path

from web.views import main_view

from web.views import registration_view

from web.views import auth_view

from web.views import logout_view

from web.views import borrow_book_edit_view

from web.views import books_view

from web.views import reader_view

from web.views import borrow_book_delete

urlpatterns = [
    path("", main_view, name = "main"),
    path("registration/",registration_view, name = "registration"),
    path("auth/",auth_view, name = "auth"),
    path("logout/", logout_view, name = "logout"),
    path("borrow/add/",borrow_book_edit_view, name = "borrow_book_add"),
    path("borrow/<int:id>/",borrow_book_edit_view, name = "borrow_book_edit"),
    path("borrow/<int:id>/delete/", borrow_book_delete, name="borrow_book_delete"),
    path("books/", books_view, name = "books"),
    path("readers/",reader_view, name = "readers"),

]
