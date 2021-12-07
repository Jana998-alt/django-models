from django.shortcuts import render
from django.views.generic import TemplateView

from snacks.models import Snack

# Create your views here.

class SnackListView(TemplateView):
    template_name = 'snack_list.html'
    model = Snack

class snack_detail(TemplateView):
    template_name = 'snack_detail.html'
    model = Snack

    