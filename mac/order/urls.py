from django.contrib import admin
from django.urls import path, include
from . import views
from .views import AddToShopCartView

urlpatterns = [
    path('', views.index, name='index'),
    path('addtoshopcart/<int:id>', AddToShopCartView.as_view(), name='addtoshopcart'),
    path('deletefromshopcart/<int:id>', views.deletefromshopcart, name='deletefromshopcart'),

]