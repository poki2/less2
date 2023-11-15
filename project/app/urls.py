from django.urls import path

from app.views import *

urlpatterns = [
    path('', start_page, name='start'),
    path('create/', CreateProductView.as_view(), name='create'),
    path('update/<slug:slug>/', UpdateProductView.as_view(), name='update'),
    path('list/', ProductListView.as_view(), name='list'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('', filter_test_view, name='filter')

]