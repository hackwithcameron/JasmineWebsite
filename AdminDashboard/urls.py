from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'admindashboard'
urlpatterns = [
    path('', views.admin_index, name='index'),
    path('<int:pk>/newpost/', views.new_post, name='new_post'),
    path('drafts/', views.drafts, name='drafts'),
]
