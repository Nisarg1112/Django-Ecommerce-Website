"""mac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import sys

sys.path.append('..')
from django.urls import path
from . import views
from .views import IndexView, AboutView, TrackView, MyAccountView, WishlistView, CompareView, LoginView, ContactView
from .views import CategoryProductView, SearchView, ProductDetailView, ShopCartView, LogoutView, SignUpView, \
    CheckoutView
from order import views as OrderViews

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('about-us/', AboutView.as_view(), name='AboutUs'),
    path('contact/', ContactView.as_view(), name='contact_us'),
    path('tracker/', TrackView.as_view(), name='track'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('addtoshopcart/', ShopCartView.as_view(), name='shopcart'),
    path('my_account/', MyAccountView.as_view(), name='my_account'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('compare/', CompareView.as_view(), name='compare'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout_func'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', IndexView.as_view(), name='home'),
    path('category/<int:id>/<slug:slug>', CategoryProductView.as_view(), name='category_products'),
    path('product/<int:id>/<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
]
