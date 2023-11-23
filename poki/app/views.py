import random as std_random

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *

from app.form import MotherboardForm
from app.models import Motherboard


# Create your views here.

def start(request):
    all_products = Motherboard.objects.all()
    random_products = std_random.sample(list(all_products), 3)
    context = {'random_products': random_products}
    return render(request, 'app_admin/base.html', context)





# class CustomLoginView(LoginView):
#     template_name = 'app_admin/login.html'
#     form_class = CustomUserChangeForm
#     success_url = reverse_lazy('start')
#
# class CustomRegisterView(CreateView):
#     template_name = 'app_admin/register.html'
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')



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
