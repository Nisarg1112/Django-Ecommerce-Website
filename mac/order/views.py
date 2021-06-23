import sys
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, DetailView, FormView, CreateView, ListView, DeleteView

sys.path.append('..')

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import ShopCart, ShopCartForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    return HttpResponse('Order Page')


class AddToShopCartView(LoginRequiredMixin, CreateView):
    model = ShopCart
    form_class = ShopCartForm

    def form_valid(self, form_class):
        url = self.request.META.get('HTTP_REFERER')
        print(url)
        current_user = self.request.user
        print(current_user)
        checkproduct = ShopCart.objects.filter(product_id=self.kwargs.get('id'))
        print(checkproduct)

        if checkproduct:
            control = 1
        else:
            control = 0

        if control == 1:
            data = ShopCart.objects.get(product_id=self.kwargs.get('id'))
            data.quantity = form_class.cleaned_data['quantity']
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = self.kwargs.get('id')
            data.quantity = form_class.cleaned_data['quantity']
            data.save()

        messages.success(self.request, 'Product added to ShopCart')
        return HttpResponseRedirect(url)

    def form_invalid(self, form_class):
        url = self.request.META.get('HTTP_REFERER')
        current_user = self.request.user
        checkproduct = ShopCart.objects.filter(product_id=self.kwargs.get('id'))

        if checkproduct:
            control = 1
        else:
            control = 0

        if control == 1:
            data = ShopCart.objects.get(product_id=self.kwargs.get('id'))
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = self.kwargs.get('id')
            data.quantity = 1
            data.save()
        messages.success(self.request, "Product Added To Shop Cart")
        return HttpResponseRedirect(url)


@login_required(login_url='/login')
def deletefromshopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, 'Item Successfully Deleted!')
    return HttpResponseRedirect(url)
