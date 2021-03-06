from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Image, Post
from .forms import BlogForm, PostForm, ImageForm


@login_required(login_url='/accounts/login/')
class Post()
def admin_index(request):
    user = request.user.get_username()
    new_blog_post = create_new_post(request)
    context = {
        'user': user,
        'new_blog_post': new_blog_post,
    }
    return render(request, 'AdminDashboard/index.html', context)


@login_required
def new_post(request, pk):
    pk = int(pk)
    blog = BlogPost.posts.all().filter(pk=pk)[0]
    text = blog.post_set
    food = blog.image_set
    text_form = PostForm(request.POST or None)
    img_form = ImageForm(request.POST or None)
    context = {
        'blog': blog,
        'text_form': text_form,
        'img_form': img_form,
        'text': text,
        'food': food,
    }
    return render(request, 'AdminDashboard/new_post.html', context)


@login_required
def drafts(request):
    blogs = BlogPost.posts.all().filter(published=False)
    new_post_form = create_new_post(request)
    context = {
        'blogs': blogs,
        'new_blog_post': new_post_form
    }
    return render(request, 'AdminDashboard/drafts.html', context)


# General function to create new blog posts
def create_new_post(request):
    if request.method == 'POST' and 'new_post' in request.POST:
        blog_form = BlogForm(request.POST or None)
        if blog_form.is_valid():
            blog_form.save()
            return render(request, 'AdminDashboard/new_post.html')
    else:
        return BlogForm()
