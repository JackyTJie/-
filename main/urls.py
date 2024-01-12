from django.urls import path
from .import views

urlpatterns = [
    path('<str:checkcode>/<str:pid>', views.m_page, name='user'),
    path('/1', views.red, name='red'),
]
