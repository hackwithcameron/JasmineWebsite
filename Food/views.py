from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *


class FoodPostList(generic.ListView):
    queryset = FoodBlogPost.posts.filter(published=True).order_by('-created_on')
    template_name = 'Food/index.html'


class FoodPostDetail(generic.DetailView):
    model = FoodBlogPost
    template_name = 'Food/post_detail.html'