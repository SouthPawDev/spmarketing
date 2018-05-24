from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, DetailView
from django.contrib.auth import login, authenticate
from login.forms import SignUpForm
from django.contrib.auth.decorators import login_required
# Create your views here.


class IndexView(TemplateView):
    template_name = 'login/index.html'


class LoginView(TemplateView):
    template_name = 'login/login.html'


class LogoutView(TemplateView):
    template_name = 'login/logout.html'


class HomeView(TemplateView):
    template_name = 'login/home.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'login/signup.html', {'form': form})
