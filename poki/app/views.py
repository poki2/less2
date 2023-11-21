from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from app.form import MotherboardForm
from app.models import Motherboard


# Create your views here.

def start(request):
    latest_product = Motherboard.objects.latest()
    context = {'latest_product': latest_product}
    return render(request, 'app_admin/base.html', context)


class MotherboardListView(ListView):
    model = Motherboard
    template_name = 'app_admin/motherboard.html'
    context_object_name = 'motherboards'


class MotherboardDetailView(DetailView):
    model = Motherboard
    template_name = 'app_admin/motherboard_detail.html'
    context_object_name = 'motherboard'

class MotherboardCreateView(CreateView):
    model = Motherboard
    template_name = 'app_admin/motherboard_create.html'
    form_class = MotherboardForm
    success_url = reverse_lazy('motherboard')


class MotherboardUpdateView(UpdateView):
    model = Motherboard
    template_name = 'app_admin/motherboard_create.html'
    form_class = MotherboardForm
    success_url = reverse_lazy('motherboard')


class MotherboardDeleteView(DeleteView):
    model = Motherboard
    template_name = 'app_admin/motherboard_delete.html'
    success_url = reverse_lazy('motherboard')
