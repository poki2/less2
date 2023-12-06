from django.urls import path

from app.views import *

urlpatterns = [
    path('', register_visitor, name='register'),
    path('thankyou', thankyou, name='thankyou')
]