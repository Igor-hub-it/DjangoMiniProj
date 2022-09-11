from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.

def home(request):
    posts = Article.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def test(request):
    return HttpResponse('<h5>its testpage</h5>')