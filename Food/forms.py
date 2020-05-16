from django.forms import ModelForm
from .models import FoodComment


class FoodCommentForm(ModelForm):
    model = FoodComment
    fields = ['author', 'comment']