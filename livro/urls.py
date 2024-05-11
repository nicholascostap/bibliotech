from django.urls import path
from livro.views import index

urlpatterns = [
    path('', index),
]