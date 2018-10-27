from django.urls import path
from .views import *

app_name = 'shopping'
# 路由
urlpatterns = [
    path('home/', go_home, name="home"),
    path('market/<categoryid>/<childcid>/<sortid>/', market, name='market'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('mine/', mine, name='mine'),
    path('quit/', logout, name='quit'),
    path('username/', username, name='username'),
    path('cart/', cart, name='cart'),
    path('sub/', sub, name='sub'),
    path('add/', add, name='add'),
    path('cart_add/', cart_add, name='cart_add'),
    path('cart_sub/', cart_sub, name='cart_sub'),
    path('click/', click, name='click'),
    path('all_click/', all_click, name='all_click'),
]
