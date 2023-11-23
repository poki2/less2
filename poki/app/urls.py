from django.urls import path

from app.views import *

urlpatterns = [
    path('motherboards/', MotherboardListView.as_view(), name='motherboard'),
    path('', start, name='start'),
    path('delete/<int:pk>/', MotherboardDeleteView.as_view(), name='delete'),
    path('create/', MotherboardCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MotherboardUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', MotherboardDetailView.as_view(), name='detail'),

]