from django.urls import path
from django.contrib.auth import views as auth_views
from login import views

app_name = 'login'

urlpatterns = [
    path('login/', auth_views.login, {'template_name': 'login/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'login/logout.html'}, name='logout'),

]
