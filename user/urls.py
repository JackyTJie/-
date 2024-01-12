from django.urls import path
from .import views

urlpatterns = [
    path('game_1', views.game_1, name='yxhf1'),
    path('<str:checkcode>/reset', views.show_reset, name='show'),
    path('<str:checkcode>/do_reset', views.reset, name='repass'),
    path('<str:checkcode>/<str:uname>', views.v_page, name='visitor'),
    path('<str:checkcode>', views.u_page, name='user_page'),
    path('/<str:uname>', views.log2, name='Res'),
    path('', views.log, name='Res'),
]
