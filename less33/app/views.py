# views.py
from django.shortcuts import render
from django.db.models import Sum
from .models import Bottle, Order, CompletedOrder, Employee, Client, Revenue

def dashboard(request):
    bottles_quantity = Bottle.objects.aggregate(total_quantity=Sum('quantity'))
    current_orders = Order.objects.all()
    completed_orders = CompletedOrder.objects.all()
    busy_employees = Employee.objects.filter(busy=True)
    free_employees = Employee.objects.filter(busy=False)
    clients = Client.objects.all()
    revenue_today = Revenue.objects.latest('date').day_revenue
    revenue_week = Revenue.objects.latest('date').week_revenue
    revenue_month = Revenue.objects.latest('date').month_revenue

    context = {
        'bottles_quantity': bottles_quantity['total_quantity'] if bottles_quantity['total_quantity'] is not None else 0,
        'current_orders': current_orders,
        'completed_orders': completed_orders,
        'busy_employees': busy_employees,
        'free_employees': free_employees,
        'clients': clients,
        'revenue_today': revenue_today,
        'revenue_week': revenue_week,
        'revenue_month': revenue_month,
    }

    return render(request, 'app/dashboard.html', context)
