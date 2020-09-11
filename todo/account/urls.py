from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.index, name='index'),
    path('login/attempt', views.view_login, name='login'),
    path('logout', views.view_logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('signup/attempt', views.new_account, name='new_account'),
]