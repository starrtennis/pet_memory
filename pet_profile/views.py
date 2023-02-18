from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)


class PetDetailView(DetailView):
    model = Pet
    template_name = "pet_details.html"