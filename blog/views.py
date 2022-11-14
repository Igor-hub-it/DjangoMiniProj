from django.shortcuts import render, get_object_or_404, redirect

from .models import Article, Category
from .forms import PostForm

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

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Article.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form,})