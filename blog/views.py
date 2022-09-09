from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requesst):
    return HttpResponse('<h1>Hello world!</h1>')

def test(request):
    return HttpResponse('<h5>its testpage</h5>')