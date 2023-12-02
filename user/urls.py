from django.urls import path
from .import views

urlpatterns = [
    path('<str:checkcode>/<str:uname>', views.v_page, name='visitor'),
    path('<str:checkcode>', views.u_page, name='user_page'),
]
