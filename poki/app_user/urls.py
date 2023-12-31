from django.urls import path

from app_user.views import *

urlpatterns = [
    path('build_pc/', build_pc, name='build_pc'),
    path('', start_page, name='start'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('detail/<int:pk>/', MotherboardDetailView.as_view(), name='detail'),
    path('motherboards/', MotherboardListView.as_view(), name='motherboard'),
    path('profile_derail/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('order/', OrderCreateView.as_view(), name='order_form'),

    path('order/<int:pk>/', OrderConfirmationView.as_view(), name='order_confirmation'),

]