from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def home(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "layouts/home.html")

def new(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "layouts/new.html")