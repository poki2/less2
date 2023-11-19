from django.urls import path

from app_admin.views import *

urlpatterns = [
    path('motherboards/', MotherboardListView.as_view(), name='motherboard'),
    path('processors/', ProcessorListView.as_view(), name='processor'),
    path('rams/', RAMListView.as_view(), name='ram'),
    path('ssds/', SSDListView.as_view(), name='ssd'),
    path('hdds/', HDDListView.as_view(), name='hdd'),
    path('graphicscards/', GraphicsCardListView.as_view(), name='graphicscard'),
    path('coolers/', CoolerListView.as_view(), name='cooler'),
    path('powersupplies/', PowerSupplyListView.as_view(), name='powersupply'),
    path('computercases/', ComputerCaseListView.as_view(), name='computercase'),
    path('', start, name='start'),
    path('delete/<slug:slug>/', MotherboardDeleteView.as_view(), name='delete'),
    path('create/', MotherboardCreateView.as_view(), name='create'),
    path('update/<slug:slug>/', MotherboardUpdateView.as_view(), name='update'),
    path('detail/', MotherboardDetailView.as_view(), name='detail')
]