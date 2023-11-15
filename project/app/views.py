from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from app.filter import ProductFilter
from app.form import ProductCreate
from app.models import Product


def start_page(request):
    return render(request, 'app/start.html')


class CreateProductView(CreateView):
    template_name = 'app/create.html'
    form_class = ProductCreate
    success_url = reverse_lazy('start')

class UpdateProductView(UpdateView):
    template_name = 'app/update.html'
    form_class = ProductCreate
    success_url = reverse_lazy('start')


class Login(LoginView):
    template_name = 'app/login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('start')


class RegisterView(CreateView):
    template_name = 'app/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('start')

class ProductListView(ListView):
    template_name = 'app/list_product.html'
    model = Product
    context_object_name = 'product'

def logout_user(request):
    logout(request)
    return redirect('start')



def filter_test_view(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    context = {'filter': f}

    return render(request, 'list_product.html', context)