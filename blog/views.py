from django.shortcuts import render, get_object_or_404
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


def get_category(request, category_id):
    posts = Article.objects.filter(category_id = category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk = category_id)
    return render(request, 'blog/category.html', {'posts': posts, 'categories': categories, 'category': category, 'title': 'ЖОПА'})

def view_post(request, post_id):
    # post = Article.objects.get(pk = post_id)
    post = get_object_or_404(Article, pk=post_id)
    return render(request, 'blog/post.html', {'post': post,})