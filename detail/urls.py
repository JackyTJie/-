from django.urls import path
from .import views

urlpatterns = [
    path('<str:checkcode>/<str:tid>/star', views.star, name='star'),
    path('<str:checkcode>/<str:tid>', views.detail, name='detail'),
]
