from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListArticle.as_view(), name='list-articles'),
    path('criar/', views.ListArticle.as_view(), name='create-articles'),
]
