from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.

def home(request):
    posts = Article.objects.all()
    title = 'Заголовок'
    data = {'posts': posts, 'title': title}
    return render(request, 'blog/home.html', data)

def test(request):
    return HttpResponse('<h5>its testpage</h5>')