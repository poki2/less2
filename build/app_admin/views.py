from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from app_admin.form import MotherboardForm
from app_admin.models import *


# Create your views here.

def start(request):
    return render(request, 'app_admin/base.html')


class MotherboardListView(ListView):
    model = Motherboard
    template_name = 'app_admin/motherboard.html'
    context_object_name = 'motherboards'


class MotherboardDetailView(DetailView):
    model = Motherboard
    template_name = 'app_admin/motherboard_detail.html'
    context_object_name = 'motherboards'

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


class ProcessorListView(ListView):
    model = Processor
    template_name = 'app_admin/processor.html'
    context_object_name = 'processors'

class RAMListView(ListView):
    model = RAM
    template_name = 'app_admin/ram.html'
    context_object_name = 'rams'

class SSDListView(ListView):
    model = SSD
    template_name = 'app_admin/ssd.html'
    context_object_name = 'ssds'

class HDDListView(ListView):
    model = HDD
    template_name = 'app_admin/hdd.html'
    context_object_name = 'hdds'

class GraphicsCardListView(ListView):
    model = GraphicsCard
    template_name = 'app_admin/graphicscard.html'
    context_object_name = 'graphicscards'

class CoolerListView(ListView):
    model = Cooler
    template_name = 'app_admin/cooler.html'
    context_object_name = 'coolers'

class PowerSupplyListView(ListView):
    model = PowerSupply
    template_name = 'app_admin/powersupply.html'
    context_object_name = 'powersupplies'

class ComputerCaseListView(ListView):
    model = ComputerCase
    template_name = 'app_admin/computercase.html'
    context_object_name = 'computercases'
