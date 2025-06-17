from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def register(request):

    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main")

    return render(request, 'user_system/register.html', context={"form":form})

def login_page(request):

    form = AuthenticationForm(request, request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect("main")

    return render(request, 'user_system/login.html', context={"form":form})