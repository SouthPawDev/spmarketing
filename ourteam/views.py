from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class OurTeam(TemplateView):
    template_name = 'misc/ourteam.html'
