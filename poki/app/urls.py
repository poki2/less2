from django.urls import path
from django.contrib.auth.decorators import permission_required
from app.views import *


urlpatterns = [
    path('motherboards/', MotherboardListView.as_view(), name='motherboard'),
    path('', start, name='start'),
    path('delete/<int:pk>/', permission_required('is_staff')(MotherboardDeleteView.as_view()), name='delete'),
    path('product/create/', permission_required('is_staff')(MotherboardCreateView.as_view()), name='create'),
    path('update/<int:pk>/', permission_required('is_staff')(MotherboardUpdateView.as_view()), name='update'),
    path('detail/<int:pk>/', MotherboardDetailView.as_view(), name='detail'),
]