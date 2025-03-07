from importlib.metadata import requires
from pydoc import render_doc

from django import forms

from django.contrib.auth import get_user_model

from web.models import Borrow

from web.models import Book

from web.models import Reader

Author = get_user_model()

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password"] != cleaned_data["password2"]:
            self.add_error("password","password must be equal")
        return cleaned_data

    class Meta:
        model = Author
        fields = ("email","username","password","password2")


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class BorrowBookForm(forms.ModelForm):
    def save(self,commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = Borrow
        fields = ("reader", "book", "borrow_date","return_date")
        widgets = {
            "borrow_date" : forms.DateTimeInput(attrs={"type":"datetime-local"}),
            "return_date" : forms.DateTimeInput(attrs={"type":"datetime-local"})
        }


class BooksForm(forms.ModelForm):
    def save(self,commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = Book
        fields = {"title","genre","author_id"}


class ReaderForm(forms.ModelForm):
    def save(self,commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = Reader
        fields = {"firstname","lastname","date_of_birth"}
        widgets = {
            "date_of_birth" : forms.DateTimeInput(attrs={"type":"datetime-local"})
        }


class BorrowBookFilter(forms.Form):
    search = forms.CharField(label = "",widget=forms.TextInput(attrs={"placeholder":"Поиск"}),required=False)
    borrow_date = forms.DateTimeField(
        label = "От",
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}
        ),
        required=False
    )
    return_date = forms.DateTimeField(
        label="До",
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}
        ),
        required=False
    )

class ImportForm(forms.Form):
    file = forms.FileField()