from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegisterForm

# Create your views here.
def login_user(response):
    return render(response, "register/login.html", {})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})

def logout(respone):
    return HttpResponse("LOGOUT")