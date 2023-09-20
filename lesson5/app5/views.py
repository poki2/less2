from django.shortcuts import render

# Create your views here.
from django.views.generic import *

from app5.models import Car


class CarCreateView(CreateView):
    templates = 'create.html'
    model = Car

class CarListView(ListView):
    templates = 'list.html'
    model = Car