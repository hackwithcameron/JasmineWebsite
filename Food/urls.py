
from django.urls import path
from . import views


urlpatterns = [
    path('', views.FoodPostList.as_view(), name='foodIndex'),
    path('<int:pk>/details', views.FoodPostDetail.as_view(), name='food_detail')
]

