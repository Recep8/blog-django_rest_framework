from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.

def register(request):
    form = RegisterForm()
    context = {
        "form": form
    }

    return render(request, "register.html", context)

def login(request):
    return render(request, "login.html")

def logout(request):
    return render(request, "logout.html")