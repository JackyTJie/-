from django.urls import path
from .import views

urlpatterns = [
    path('', views.red, name='redirect'),
    path('comment/<str:checkcode>/<str:tid>', views.com, name='comment'),
    path('comment//<str:tid>', views.red1, name='red1'),
    path('thumb/<str:checkcode>/<str:tid>/<str:thid>', views.thumb, name='thumb'),
    path('thumb//<str:tid>/<str:thid>', views.red2, name='red2'),
]
