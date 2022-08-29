from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("/")

        messages.error(request, "Unsuccessful registration. Please check blanks and try again")
    form = RegisterForm()

    return render(request=request, template_name="register.html", context={"register_form": form})

