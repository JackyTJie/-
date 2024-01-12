from django.urls import path
from .import views

urlpatterns = [
    path('<str:checkcode>/<str:tid>/unstar', views.unstar, name='unstar'),
    path('<str:checkcode>/<str:tid>/star', views.star, name='star'),
    path('<str:checkcode>/<str:tid>/gift', views.show_gift, name='gift'),
    path('<str:checkcode>/<str:tid>/send_gift', views.gift, name='do_gift'),
    path('<str:checkcode>/<str:tid>', views.detail, name='detail'),
    path('/<str:tid>/star', views.red, name='red'),
]
