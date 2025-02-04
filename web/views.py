from django.shortcuts import render, redirect
from django.http import HttpResponse

from web.forms import RegistrationForm
from web.forms import AuthForm

from django.contrib.auth import get_user_model, authenticate, login, logout

Author = get_user_model()

# Create your views here.

def main_view(request):
    return render(request,"web/main.html")

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