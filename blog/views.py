from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Category
from .forms import PostForm, CategoryForm


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def categories(request):
    """list for categories"""
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'blog/categories.html', context)


def new_category(request):
    """Add a new category"""
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            Category.objects.create(text=text)
            return redirect('blog:new_post')
    context = {'form': form}
    return render(request, 'blog/new_category.html', context)


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
