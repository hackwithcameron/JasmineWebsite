from django.forms import ModelForm
from .models import Comment, Post, BlogPost, Image


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'comment']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['section']


class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['cover_image', 'category', 'title', 'description', 'published']


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']
