from django.urls import path, include , re_path, reverse
from django.contrib.auth import views as auth_views
from login import views

app_name = 'login'

urlpatterns = [
    path('login/', auth_views.login, {'template_name': 'login/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'login/logout.html'}, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', auth_views.password_reset, {'template_name': 'login/password_reset_form.html'},
         name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done, {'template_name': 'login/password_reset_done.html'},
         name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.password_reset_confirm, name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
