import self as self
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render, redirect
# Create your views here.


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from app.models import *
from app_user.form import RegistrationForm, LoginForm, OrderForm
from app_user.models import CustomUser, Order, CartItem, Cart


def build_pc(request):
    motherboards = Motherboard.objects.all()
    processors = Processor.objects.all()
    rams = RAM.objects.all()
    ssds = SSD.objects.all()
    hdds = HDD.objects.all()
    graphics_cards = GraphicsCard.objects.all()
    coolers = Cooler.objects.all()
    power_supplies = PowerSupply.objects.all()
    computer_cases = ComputerCase.objects.all()

    context = {
        'motherboards': motherboards,
        'processors': processors,
        'rams': rams,
        'ssds': ssds,
        'hdds': hdds,
        'graphics_cards': graphics_cards,
        'coolers': coolers,
        'power_supplies': power_supplies,
        'computer_cases': computer_cases,
    }

    if request.method == 'POST':
        selected_motherboard_id = request.POST.get('motherboard', None)
        selected_processor_id = request.POST.get('processor', None)
        selected_ram_id = request.POST.get('ram', None)
        selected_hdd_id = request.POST.get('hdd', None)
        selected_graphic_card_id = request.POST.get('graphics_card', None)
        selected_cooler_id = request.POST.get('cooler', None)
        selected_power_supplie_id = request.POST.get('power_supplie', None)
        selected_computer_case_id = request.POST.get('computer_cases', None)

        selected_motherboard = Motherboard.objects.get(pk=selected_motherboard_id)
        selected_processor = Processor.objects.get(pk=selected_processor_id)
        selected_ram = RAM.objects.get(pk=selected_ram_id)
        selected_hdd = HDD.objects.get(pk=selected_hdd_id)
        selected_graphic_card = GraphicsCard.objects.get(pk=selected_graphic_card_id)
        selected_cooler = Cooler.objects.get(pk=selected_cooler_id)
        selected_power_supplie = PowerSupply.objects.get(pk=selected_power_supplie_id)
        selected_computer_case = ComputerCase.objects.get(pk=selected_computer_case_id)

        if selected_motherboard.socket != selected_processor.socket:
            context['compatibility_error'] = 'Материнская плата и процессор не совместимы.'

        if 'compatibility_error' not in context:
            context['selected_motherboard'] = selected_motherboard.get_component_info()
            context['selected_processor'] = selected_processor.get_component_info()
            context['selected_ram'] = selected_ram.get_component_info()
            context['selected_hdd'] = selected_hdd.get_component_info()
            context['selected_graphic_card'] = selected_graphic_card.get_component_info()
            context['selected_cooler'] = selected_cooler.get_component_info()
            context['selected_power_supplie'] = selected_power_supplie.get_component_info()
            context['selected_computer_case'] = selected_computer_case.get_component_info()

    return render(request, 'app_user/build_pc.html', context)


import random as std_random


def start_page(request):
    all_motherboards = Motherboard.objects.all()
    all_processors = Processor.objects.all()
    all_powersupply = PowerSupply.objects.all()
    all_ram = RAM.objects.all()
    all_ssd = SSD.objects.all()
    all_hdd = HDD.objects.all()
    all_cooler = Cooler.objects.all()
    all_case = ComputerCase.objects.all()
    all_graphiccart = GraphicsCard.objects.all()

    all_products = list(all_motherboards)

    random_products = std_random.sample(all_products, 3)
    context = {'random_products': random_products}
    return render(request, 'app_user/start.html', context)


class Login(LoginView):
    template_name = 'app_user/login.html'
    form_class = LoginForm
    next_page = reverse_lazy('start')


class RegisterView(CreateView):
    template_name = 'app_user/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


def logout_user(request):
    logout(request)
    return redirect('start')


class MotherboardListView(ListView):
    model = Motherboard
    template_name = 'app/motherboard.html'
    context_object_name = 'motherboards'


class MotherboardDetailView(DetailView):
    model = Motherboard
    template_name = 'app/motherboard_detail.html'
    context_object_name = 'motherboard'


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'app_user/order.html'
    success_url = reverse_lazy('order_confirmation')




class OrderConfirmationView(DetailView):
    model = Order
    template_name = 'app_user/order_confirmation.html'
    context_object_name = 'order'


class ProfileDetail(DetailView):
    model = CustomUser
    template_name = 'app_user/profile_detail.html'
    context_object_name = 'profiles'