
from django.urls import path
from . import views


urlpatterns = [
    path('', views.FoodPostList.as_view(), name='food_index'),
    path('<int:pk>/details', views.food_detail, name='food_detail'),
]

