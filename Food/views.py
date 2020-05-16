from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from .models import *


class FoodPostList(generic.ListView):
    queryset = FoodBlogPost.posts.filter(published=True).order_by('-created_on')
    template_name = 'Food/index.html'


class FoodPostDetail(generic.DetailView):
    model = FoodBlogPost
    template_name = 'Food/post_detail.html'


def food_detail(request, pk):
    pk = int(pk)

    blog = get_object_or_404(FoodBlogPost, pk=pk)
    images = get_list_or_404(blog.foodimage_set)
    sections = get_list_or_404(blog.foodpost_set)
    post = zip(sections, images)

    context = {
        'blog': blog,
        'post': post,
    }
    return render(request, 'Food/post_detail.html', context)





