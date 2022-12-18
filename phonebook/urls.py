from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('display/<int:pk>', views.display, name='display'),
]