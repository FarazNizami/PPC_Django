from django.urls import path
from django.contrib import admin
from . import views
from .views import blastfurnace

urlpatterns = [
    path('', views.home, name='home'),  # Home page after login
    path('admin/', admin.site.urls), 
    path('blast_furnace/', blastfurnace, name='blastfurnace'),
    path('login/', views.user_login, name='login'),  # Added login path
]
