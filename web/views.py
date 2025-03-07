from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render, redirect
from django.http import HttpResponse

from web.forms import RegistrationForm
from web.forms import AuthForm

from django.contrib.auth import get_user_model, authenticate, login, logout

from web.forms import BorrowBookForm

from web.models import Borrow

from web.models import Book

from web.forms import BooksForm

from web.models import Reader

from web.forms import ReaderForm

from web.forms import BorrowBookFilter

from web.forms import ImportForm
from web.services import filter_borrow_book

from web.services import import_book_from_csv

from web.services import export_book_csv

Author = get_user_model()

# Create your views here.

def main_view(request):
    borrow = Borrow.objects.all()

    filter_form = BorrowBookFilter(request.GET)
    filter_form.is_valid()
    borrow = filter_borrow_book(borrow,filter_form.cleaned_data)

    total_count = borrow.count()

    borrow = borrow.prefetch_related("reader").select_related("book").annotate(spent_time = F("return_date") - F("borrow_date"))

    page_number = request.GET.get("page",1)
    paginator = Paginator(borrow,per_page = 10)

    if request.GET.get('export') == 'csv':
        response = HttpResponse(
            content_type='text/csv',
            headers={"Content-Disposition": "attachment; filename=book_borrow.csv"}
        )
        return export_book_csv(borrow, response)

    return render(request,"web/main.html", {"borrow":paginator.get_page(page_number),
                                            "form": BorrowBookForm(),
                                            "filter_form": filter_form,
                                            "total_count":total_count})

def import_view(request):
    if request.method == 'POST':
        form = ImportForm(files = request.FILES)
        if form.is_valid():
            import_book_from_csv(form.cleaned_data['file'])
            return redirect("main")
    return render(request,"web/import.html",
                  {"form":ImportForm})

def registration_view(request):
    form = RegistrationForm
    is_success = False
    if request.method == "POST":
        form = RegistrationForm(data = request.POST)
        if form.is_valid():
            author = Author(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
            )
            author.set_password(form.cleaned_data['password'])
            author.save()
            print(form.cleaned_data)
            is_success = True
    return render(request,"web/registration.html",{"form":form,
                                                   "is_success": is_success} )


def auth_view(request):
    form = AuthForm()
    if request.method == "POST":
        form = AuthForm(data = request.POST)
        if form.is_valid():
            author = authenticate(**form.cleaned_data)
            if author is None:
                form.add_error(None,"unknown author")
            else:
                login(request,author)
                return redirect("main")
    return render(request,"web/auth.html",{"form":form})


def logout_view(request):
    logout(request)
    return redirect("main")


def borrow_book_edit_view(request, id = None):
    borrow = Borrow.objects.get(id = id) if id is not None else None
    form = BorrowBookForm(instance=borrow)
    if request.method == 'POST':
        form = BorrowBookForm(data=request.POST,initial = {"user": request.user})
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request,"web/borrow_book_form.html", {"form":form})


def _list_editor_view(request, model_cls, form_cls, template_name, url_name):
    items = model_cls.objects.all()
    form = form_cls()
    if request.method == 'POST':
        form = form_cls(data=request.POST, initial={"user": request.user})
    if form.is_valid():
        form.save()
        return redirect(url_name)
    return render(request, f"web/{template_name}.html", {"items": items, "form": form})


def books_view(request):
    return _list_editor_view(request, Book, BooksForm, "book_form","books")


def reader_view(request):
    return _list_editor_view(request, Reader, ReaderForm, "reader_form","readers")

def  borrow_book_delete(request,id):
    borrow = Borrow.objects.get(id = id)
    borrow.delete()
    return redirect('main')








