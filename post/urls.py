from django.urls import path
from .import views

urlpatterns = [
    path('<str:checkcode>', views.post_a, name='submit'),
    path('article/<str:checkcode>', views.post_A, name='article'),
    path('message/<str:checkcode>', views.post_M, name='message'),
]
