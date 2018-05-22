from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'login/index.html'


class LoginView(TemplateView):
    template_name = 'login/login.html'


class LogoutView(TemplateView):
    template_name = 'login/logout.html'

