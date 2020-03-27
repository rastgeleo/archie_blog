from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post, Category
from .forms import PostForm, CategoryForm


def index(request):
    posts = Post.objects.all()[:5]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def categories(request, category_id=None):
    """list view by categories"""
    categories = Category.objects.all()
    if category_id:
        posts = Post.objects.filter(category__id=category_id)
    else:
        posts = Post.objects.all()
    context = {
        'categories': categories,
        'posts': posts,
        'category_id': category_id
    }
    return render(request, 'blog/categories.html', context)


@login_required
def new_category(request):
    """Add a new category"""
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            Category.objects.create(text=text)
            return redirect('blog:categories')
    context = {'form': form}
    return render(request, 'blog/new_category.html', context)


@login_required
def edit_category(request, category_id):
    """Edit an existing category"""
    category = get_object_or_404(Category, pk=category_id)
    if request.method != 'POST':
        form = CategoryForm(instance=category)
    else:
        form = CategoryForm(instance=category, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('blog:categories')
    context = {'form': form, 'category': category}
    return render(request, 'blog/edit_category.html', context)


@login_required
def new_post(request):
    """Add a new post"""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save()
            return redirect('blog:detail', post_id=new_post.id)

    # Display a blank form or invalid form.
    context = {'form': form}
    return render(request, 'blog/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """Edit the existing post"""
    post = get_object_or_404(Post, pk=post_id)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('blog:detail', post_id=post.id)
    context = {'form': form, 'post': post}
    return render(request, 'blog/edit_post.html', context)
