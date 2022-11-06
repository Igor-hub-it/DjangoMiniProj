from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category

# Create your views here.

def home(request):
    posts = Article.objects.all()
    title = 'Заголовок'
    categories = Category.objects.all()
    data = {
        'posts': posts,
        'title': title,
        'categories': categories,
    }
    return render(request, 'blog/home.html', data)

def test(request):
    return HttpResponse('<h5>its testpage</h5>')

def get_category(request, category_id):
    posts = Article.objects.filter(category_id = category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk = category_id)
    return render(request, 'blog/category.html', {'posts': posts, 'categories': categories, 'category': category})