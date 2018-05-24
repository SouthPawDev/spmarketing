from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ourteam import models
# Create your views here.


# VIEWS FOR SMRS

class OurTeam(TemplateView):
    template_name = 'ourteam/ourteam.html'


class SmrListView(ListView):
    context_object_name = 'smrs'
    model = models.Smr


class SmrDetailView(DetailView):
    context_object_name = 'smrs_detail'
    models = models.Smr
    template_name = 'ourteam/ourteam.html'


class SmrCreateView(CreateView):
    fields = ('smr_pic', 'name', 'territory', 'car', 'franchise')
    model = models.Smr


class SmrUpdateView(UpdateView):
    fields = ('smr_pic', 'car')
    model = models.Smr


class SmrDeleteView(DeleteView):
    model = models.Smr
    success_url = reverse_lazy("ourteam")


# VIEWS FOR FRANCHISES

class FranchiseListView(ListView):
    context_object_name = 'franchises'
    model = models.Franchises


class FranchiseDetailView(DetailView):
    context_object_name = 'franchise_detail'
    model = models.Franchises
    template_name = 'ourteam/franchises_detail.html'


class FranchiseCreateView(CreateView):
    fields = ('name', 'location', 'phone_number')
    model = models.Franchises
    success_url = reverse_lazy('ourteam:franchise_list')


class FranchiseUpdateView(UpdateView):
    fields = 'phone_number'
    model = models.Franchises


class FranchiseDeleteView(DeleteView):
    model = models.Franchises
    success_url = reverse_lazy('ourteam:ourteam')


# VIEWS FOR CARS


class CarCreateView(CreateView):
    fields = ('brand', 'car_model', 'car_number')
    model = models.Cars


class CarUpdateView(UpdateView):
    fields = 'car_number'
    model = models.Cars


class CarDeleteView(DeleteView):
    model = models.Cars
    success_url = reverse_lazy('ourteam:ourteam')
