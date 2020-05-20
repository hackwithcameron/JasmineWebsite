from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from AdminDashboard.models import BlogPost
from itertools import cycle


class FoodPostList(generic.ListView):
    queryset = BlogPost.posts.filter(category=1, published=True).order_by('-created_on')
    template_name = 'Food/index.html'


class FoodPostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'Food/post_detail.html'


def food_detail(request, pk):
    pk = int(pk)

    blog = get_object_or_404(BlogPost, pk=pk)
    images = get_list_or_404(blog.image_set)
    sections = get_list_or_404(blog.post_set)
    post = zip(sections, cycle(images)) if len(sections) > len(images) else zip(cycle(sections), images)

    context = {
        'blog': blog,
        'post': post,
    }
    return render(request, 'Food/post_detail.html', context)





