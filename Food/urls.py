
from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.FoodPostList.as_view(), name='index'),
    path('<int:pk>/details', views.food_detail, name='detail'),
]

