from django.urls import path
from .import views

urlpatterns = [
    path('<str:checkcode>', views.post_a, name='submit'),
    path('post_article/<str:checkcode>', views.post_A, name='operate'),
]
