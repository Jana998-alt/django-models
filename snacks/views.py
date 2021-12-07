from django.shortcuts import render
from django.views.generic import (DetailView, ListView)

from snacks.models import Snack

# Create your views here.

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class snack_detail_view(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

