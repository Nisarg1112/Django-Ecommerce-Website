import sys
from django.forms import ModelForm

sys.path.append('..')
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from product.models import Product


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    print(user)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    print(product)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.quantity * self.product.price)


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']


class Order(models.Model):
    STATUS = (('New', 'New'), ('Accepted', 'Accepted'), ('Preparing', 'Preparing'), ('Onshipping', 'Onshipping'),
              ('Completed', 'Completed'), ('Canceled', 'Canceled'))
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=20, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100, default='nisargtrivedi054@gmail.com')
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=20)
    city = models.CharField(blank=True, max_length=20)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    country = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    zip_code = models.CharField(blank=True, max_length=20)
    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    total = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'city', 'state', 'country', 'zip_code']


class OrderProduct(models.Model):
    STATUS = (('New', 'New'), ('Accepted', 'Accepted'), ('Canceled', 'Canceled'))
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title
