from pipes import Template
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View



class HomeView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



