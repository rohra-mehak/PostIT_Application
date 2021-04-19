from django.shortcuts import render, redirect
from django.http import HttpResponse
# from . import forms as f
from postIt.forms import RegistrationForm
# from forms import RegistrationForm


def index(request):
    if request.user.is_authenticated:
        return render(request, "registration/logout.html")
# Create your views here.


def register(response):
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        print(1)
        if form.is_valid():
            print(2)
            form.save()
        # return redirect('postIt/index')
        # return HttpResponse("Hello, world. You're at the POST IT WELCOME PAGE.")
    else:
        form = RegistrationForm()

    return render(response, "register/register.html", {"form": form})
