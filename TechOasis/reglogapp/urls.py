from django.urls import path
from reglogapp.views import *


urlpatterns = [
    path('', show_start_page, name='mainp'),
    path('register/', register_page, name='reg'),
    path('login/', show_login_page, name='log'),
]

