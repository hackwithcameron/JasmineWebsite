from django.forms import ModelForm
from .models import FoodComment, FoodPost, FoodBlogPost, FoodImage


class FoodCommentForm(ModelForm):
    class Meta:
        model = FoodComment
        fields = ['author', 'comment']


class FoodPostForm(ModelForm):
    class Meta:
        model = FoodPost
        fields = ['section']


class FoodBlogForm(ModelForm):
    class Meta:
        model = FoodBlogPost
        fields = ['cover_image', 'title', 'description', 'published']


class FoodImageForm(ModelForm):
    class Meta:
        model = FoodImage
        fields = ['image']
