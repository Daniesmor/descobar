from django.urls import path
from . import views

urlpatterns = [
    #path('', views.projects, name="projects"),
    path('category/<int:category_id>/', views.category, name="category"),
    path('post_title/<post_title>/', views.projects, name="projects"),
]

