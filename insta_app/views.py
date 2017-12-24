from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from .models import Post
from .forms import PostForm


def index(request):
    if request.user.is_authenticated:
        context = {
            "user": request.user
        }
    else:
        context = {
            "user": "Guest"
        }
    return render(request, "root/index.html", context=context)


def post_index(request):
    context = {
        "title": "home",
        "posts": Post.objects.all()
    }
    return render(request, "post/post_index.html", context=context)


def post_add(request):
    if request.method == "GET" and request.user.is_authenticated:
        form = PostForm()
        context = {'form': form}
        return render(request, "post/post_form.html", context=context)
    elif request.user.is_authenticated:  # POST
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post elave olundu...')
        return redirect("insta_app:post_index")


def post_details(request, slug):
    context = {"post": get_object_or_404(Post, slug=slug)}
    return render(request, "post/post_details.html", context=context)


def post_update(request, slug):
    if request.method == "GET":
        _post = get_object_or_404(Post, slug=slug)
        form = PostForm(instance=_post)
        context = {'form': form, 'update': True}
        return render(request, "post/post_form.html", context=context)
    else:
        _post = get_object_or_404(Post, slug=slug)
        form = PostForm(request.POST, instance=_post)
        if form.is_valid():
            form.save()
        messages.success(request, '%s deyisildi...' % _post.title)
        return HttpResponseRedirect(_post.get_absolute_url())


def post_delete(request, slug):
    _post = get_object_or_404(Post, slug=slug)
    messages.success(request, '%s silindi...' % _post.title)
    _post.delete()
    return redirect("insta_app:post_index")
