from django.urls import path
from .import views

urlpatterns = [
    path('', views.red, name='redirect'),
    path('comment/<str:checkcode>/<str:tid>', views.com, name='comment'),
    path('thumb/<str:checkcode>/<str:tid>/<str:thid>', views.thumb, name='thumb'),
]
