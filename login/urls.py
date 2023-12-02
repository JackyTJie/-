from django.urls import path
from .import views

urlpatterns = [
    path('', views.login, name='login'),
    path('checkupdate', views.checkupdate, name='secure'),
    path('register', views.register, name='register'),
    path('reg_op', views.reg_op, name='reg_op'),
]
