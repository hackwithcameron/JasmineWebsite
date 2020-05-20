from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Food.models import FoodBlogPost, FoodImage, FoodPost
from Food.forms import FoodBlogForm, FoodPostForm, FoodImageForm


@login_required(login_url='/accounts/login/')
def admin_index(request):
    user = request.user.get_username()
    if request.method == 'POST' and 'new_post' in request.POST:
        blog_form = FoodBlogForm(request.POST or None)
        if blog_form.is_valid():
            blog_form.save()
            pk = blog_form.pk
            context = {'pk': pk}
            return render(request, 'AdminDashboard/new_post.html', context)
    else:
        print('2')
        blog_form = FoodBlogForm()
    context = {
        'user': user,
        'blog': blog_form,
    }
    return render(request, 'AdminDashboard/index.html', context)


@login_required
def new_post(request, pk):
    pk = int(pk)
    blog = get_object_or_404(FoodBlogPost, pk=pk)
    text = get_list_or_404(FoodPost, post=blog)
    food = get_list_or_404(FoodImage, post=blog)
    text_form = FoodPostForm(request.POST or None)
    img_form = FoodImageForm(request.POST or None)
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
    blogs = FoodBlogPost.posts.all().filter(published=False)
    context = {
        'blogs': blogs
    }
    return render(request, 'AdminDashboard/drafts.html', context)
