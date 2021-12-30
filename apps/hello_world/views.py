from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def home(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "layouts/home.html")

def new(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "layouts/new.html")


def login(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "accounts/login.html")


def register(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "accounts/register.html")


def logout(request):
    # return HttpResponse('Hello from Python!')
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request, "index.html")

def contact(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "legal/contact.html")


def privacy(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "legal/privacy.html")

def terms(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "legal/terms.html")

def services(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "home/services.html")

def sponsored_page(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "home/sponsored_page.html")