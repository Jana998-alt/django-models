from django.shortcuts import render
from django.views.generic import TemplateView

from snacks.models import Snack

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    model = Snack