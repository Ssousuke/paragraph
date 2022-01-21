from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListAuthor.as_view(), name='list-author'),
]
