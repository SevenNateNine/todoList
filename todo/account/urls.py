from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.index, name='index'),
    path('login/attempt', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signup/attempt', views.new_account, name='new_account'),
]