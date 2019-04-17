from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import SignupModelForm

# Create your views here.

def home_view(request):
    return render(request, "home.html")

def about_view(request):
    return render(request, "about.html")

def signup_view(request):
    form = SignupModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Thanks for signing up!")
        return redirect('/')
    context = {"form":form}
    print(context)
    return render(request, "signup.html", context)