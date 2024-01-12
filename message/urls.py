from django.urls import path
from .import views

urlpatterns = [
    path('<str:checkcode>', views.index, name='index'),
    path('send/<str:checkcode>', views.mes, name='post'),
]
