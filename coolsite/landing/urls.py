from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('work/', work, name='work'),
    path('secret_master/', secret_master,  name='secret_master'),
]