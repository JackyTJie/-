from django.urls import path
from .import views

urlpatterns = [
    path('<str:checkcode>', views.admincheck, name='admin'),
    path('<str:checkcode>/u/edit/<str:tid>', views.show_edit, name='edit_page'),
    path('<str:checkcode>/<str:item>/del/<str:tid>', views.delete, name='del'),
    path('<str:checkcode>/<str:item>/edit/<str:tid>', views.edit, name='edit'),
]
