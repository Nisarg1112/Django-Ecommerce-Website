import base64

import os
import pdfkit
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
from celery import shared_task
import sys
import jinja2
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.views.generic import View, TemplateView, DetailView, FormView, CreateView, ListView

sys.path.append('..')
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact_Message
from django.template import RequestContext
from product.models import Brand
from product.models import Category, Product, Image
from order.models import ShopCart, OrderForm, Order, OrderProduct, ShopCartForm
from .forms import SearchForm
from user.models import UserProfile
from user.forms import SignUpForm
from time import sleep
from django.shortcuts import get_object_or_404


class IndexView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, *args, **kwargs):
        products_slider = Product.objects.all().order_by('id')[:3]
        products_best_sellers = Product.objects.all().order_by('-id')
        products_recommend = Product.objects.all().order_by('?')
        category = Category.objects.all()
        current_user = self.request.user
        cart = ShopCart.objects.filter(user_id=current_user.id)
        total = 0
        count = 0
        for rs in cart:
            total += rs.product.price * rs.quantity
            count += 1
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['category'] = category
        context['products_slider'] = products_slider
        context['products_best_sellers'] = products_best_sellers
        context['products_recommend'] = products_recommend
        context['total'] = total
        context['count'] = count
        return context


class AboutView(TemplateView):
    template_name = "shop/about-us.html"

    def get_context_data(self, *args, **kwargs):
        products_slider = Product.objects.all().order_by('id')[:3]
        products_best_sellers = Product.objects.all().order_by('-id')
        products_recommend = Product.objects.all().order_by('?')
        category = Category.objects.all()
        current_user = self.request.user
        cart = ShopCart.objects.filter(user_id=current_user.id)
        total = 0
        count = 0
        for rs in cart:
            total += rs.product.price * rs.quantity
            count += 1
        context = super(AboutView, self).get_context_data(*args, **kwargs)
        context['category'] = category
        context['products_slider'] = products_slider
        context['products_best_sellers'] = products_best_sellers
        context['products_recommend'] = products_recommend
        context['total'] = total
        context['count'] = count
        return context


class TrackView(TemplateView):
    template_name = "shop/order-tracking.html"

    def get_context_data(self, *args, **kwargs):
        products_slider = Product.objects.all().order_by('id')[:3]
        products_best_sellers = Product.objects.all().order_by('-id')
        products_recommend = Product.objects.all().order_by('?')
        category = Category.objects.all()
        current_user = self.request.user
        cart = ShopCart.objects.filter(user_id=current_user.id)
        total = 0
        count = 0
        for rs in cart:
            total += rs.product.price * rs.quantity
            count += 1
        context = super(TrackView, self).get_context_data(*args, **kwargs)
        context['category'] = category
        context['products_slider'] = products_slider
        context['products_best_sellers'] = products_best_sellers
        context['products_recommend'] = products_recommend
        context['total'] = total
        context['count'] = count
        return context


class MyAccountView(TemplateView):
    template_name = "shop/my-account.html"

    def get_context_data(self, *args, **kwargs):
        products_slider = Product.objects.all().order_by('id')[:3]
        products_best_sellers = Product.objects.all().order_by('-id')
        products_recommend = Product.objects.all().order_by('?')
        category = Category.objects.all()
        current_user = self.request.user
        cart = ShopCart.objects.filter(user_id=current_user.id)
        total = 0
        count = 0
        for rs in cart:
            total += rs.product.price * rs.quantity
            count += 1
        context = super(MyAccountView, self).get_context_data(*args, **kwargs)
        context['category'] = category
        context['products_slider'] = products_slider
        context['products_best_sellers'] = products_best_sellers
        context['products_recommend'] = products_recommend
        context['total'] = total
        context['count'] = count
        return context


class WishlistView(TemplateView):
    template_name = "shop/wishlist.html"

    def get_context_data(self, *args, **kwargs):
        products_slider = Product.objects.all().order_by('id')[:3]
        products_best_sellers = Product.objects.all().order_by('-id')
        products_recommend = Product.objects.all().order_by('?')
        category = Category.objects.all()
        current_user = self.request.user
        cart = ShopCart.objects.filter(user_id=current_user.id)
        total = 0
        count = 0
        for rs in cart:
            total += rs.product.price * rs.quantity
            count += 1
        context = super(WishlistView, self).get_context_data(*args, **kwargs)
        context['category'] = category
        context['products_slider'] = products_slider
        context['products_best_sellers'] = products_best_sellers
        context['products_recommend'] = products_recommend
        context['total'] = total
        context['count'] = count
        return context


class CompareView(TemplateView):
    template_name = "shop/compare.html"

    def get_context_data(self, *args, **kwargs):
        products_slider = Product.objects.all().order_by('id')[:3]
        products_best_sellers = Product.objects.all().order_by('-id')
        products_recommend = Product.objects.all().order_by('?')
        category = Category.objects.all()
        current_user = self.request.user
        cart = ShopCart.objects.filter(user_id=current_user.id)
        total = 0
        count = 0
        for rs in cart:
            total += rs.product.price * rs.quantity
            count += 1
        context = super(CompareView, self).get_context_data(*args, **kwargs)
        context['category'] = category
        context['products_slider'] = products_slider
        context['products_best_sellers'] = products_best_sellers
        context['products_recommend'] = products_recommend
        context['total'] = total
        context['count'] = count
        return context


class LoginView(View):
    def get(self, request):
        return render(request, 'shop/login-register.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                current_user = request.user
                userprofile = UserProfile.objects.get(user_id=current_user.id)
                request.session['userimage'] = userprofile.image.url
                return HttpResponseRedirect('/')
            else:
                print('not')
                messages.warning(request, "Incorrect Username or Password entered!")
                return HttpResponseRedirect('/login')


class ContactView(CreateView):
    template_name = 'shop/contact.html'
    model = Contact_Message
    success_url = '/home'
    fields = ['name', 'email', 'subject', 'message']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CategoryProductView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = super(CategoryProductView, self).get_queryset()
        return qs.filter(category_id=self.kwargs.get('id'))

    def get_context_data(self, *args, **kwargs):
        category = Category.objects.all()
        current_user = self.request.user
        cart = ShopCart.objects.filter(user_id=current_user.id)
        total = 0
        count = 0
        for rs in cart:
            total += rs.product.price * rs.quantity
            count += 1
        context = super(CategoryProductView, self).get_context_data(*args, **kwargs)
        context['category'] = category
        context['total'] = total
        context['count'] = count
        return context


class SearchView(ListView):
    template_name = 'shop/search_products.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        search_query = self.request.GET.get('query', None)
        search_result = Product.objects.filter(title__icontains=search_query)
        return search_result

    def get_context_data(self, *args, **kwargs):
        category = Category.objects.all()
        current_user = self.request.user
        cart = ShopCart.objects.filter(user_id=current_user.id)
        total = 0
        count = 0
        for rs in cart:
            total += rs.product.price * rs.quantity
            count += 1
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        context['category'] = category
        context['total'] = total
        context['count'] = count
        return context


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)
        results = []
        for rs in products:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_details.html'
    form_class = ShopCartForm

    def get_context_data(self, *args, **kwargs):
        current_user = self.request.user
        cart = ShopCart.objects.filter(user_id=current_user.id)
        total = 0
        count = 0
        for rs in cart:
            total += rs.product.price * rs.quantity
            count += 1
        product = Product.objects.get(pk=self.kwargs.get('id'))
        category = Category.objects.all()
        image = Image.objects.filter(product_id=self.kwargs.get('id'))
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        form = ShopCartForm()
        context['category'] = category
        context['total'] = total
        context['count'] = count
        context['product'] = product
        context['image'] = image
        context['form'] = form
        return context


class ShopCartView(TemplateView):
    model = ShopCart
    template_name = 'shop/cart.html'

    def get_context_data(self, *args, **kwargs):
        category = Category.objects.all()
        print(category)
        current_user = self.request.user
        print(current_user)
        cart = ShopCart.objects.filter(user_id=current_user.id)
        print(cart)
        total = 0
        for rs in cart:
            total += rs.product.price * rs.quantity
        print(total)
        context = super(ShopCartView, self).get_context_data(*args, **kwargs)
        grand_total = total + (total * 0.18)
        context['category'] = category
        context['shopcart'] = cart
        context['total'] = total
        context['grand_total'] = grand_total
        return context


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class SignUpView(CreateView):
    template_name = 'shop/signup.html'
    form_class = SignUpForm

    def form_valid(self, form_class):
        form_class.save()
        username = form_class.cleaned_data.get('username')
        print(username)
        password = form_class.cleaned_data.get('password1')
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect('/')

        current_user = self.request.user
        data = UserProfile()
        data.user_id = current_user.id
        data.image = r'C:\Users\Nisarg Trivedi\PycharmProjects\MyAwesomeCart\mac\shop\static\user.png'
        data.save()

        return super().form_valid(form_class)


@shared_task()
def send_mail_task(code, source, target_email, name, output):

    hi = os.environ.get('SENDGRID_API_KEY')
    api = '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'
    print(hi)
    order_code = code
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_file(source, output, configuration=config)
    print(order_code)
    print(target_email)

    receiver = target_email
    user_name = name
    head = """
    <strong>Hello, Greetings From Nisarg Trivedi!</strong> We have received your order and hereby, We have shared your shopping bill. Your order will be delivered within 5-6 working days! Thank You for shopping with us, Have A Good Day'
    """

    message = Mail(
        from_email='nisargtrivedi054@gmail.com',
        to_emails=receiver,
        subject='Your Order Has Been Received',
        html_content=head)

    file = output
    with open(file, 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName('Shopping Bill.pdf'),
        FileType('application/pdf'),
        Disposition('attachment')
    )
    message.attachment = attachedFile

    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
    print('mail done')
    return None


bill = {'Product': [], 'Total': None, 'Grand Total(with GST)': None, 'Name': None,
        'Address': None, 'Order Code': None}


class CheckoutView(CreateView):
    template_name = 'shop/checkout.html'
    form_class = OrderForm

    def get_context_data(self, *args, **kwargs):
        category = Category.objects.all()

        current_user = self.request.user
        cart = ShopCart.objects.filter(user_id=current_user.id)
        print(cart)
        total = 0

        for rs in cart:
            product_dict = {'product': rs.product.title, 'quantity': rs.quantity, 'amount': None}
            bill_amount = rs.product.price * rs.quantity
            product_dict['amount'] = bill_amount
            bill['Product'].append(product_dict)
            print(rs.product)
            print(rs.quantity)
            print(rs.product.price)
            total += rs.product.price * rs.quantity

        grand_total = total + (total * 0.18)
        context_1 = {
            'shopcart': cart,
            'total': total,
            'grand_total': grand_total
        }
        bill['Total'] = total
        bill['Grand Total(with GST)'] = grand_total
        print(bill)

        form = OrderForm()
        context = super(CheckoutView, self).get_context_data(*args, **kwargs)
        context['category'] = category
        context['total'] = total
        context['shopcart'] = cart
        context['grand_total'] = grand_total
        context['form'] = form
        return context

    def form_valid(self, form_class):
        data = Order()
        current_user = self.request.user
        category = Category.objects.all()
        cart = ShopCart.objects.filter(user_id=current_user.id)
        total = 0
        for rs in cart:
            total += rs.product.price * rs.quantity
        data.first_name = form_class.cleaned_data['first_name']
        print(data.first_name)
        print(type(data.first_name))
        data.last_name = form_class.cleaned_data['last_name']
        data.address = form_class.cleaned_data['address']
        data.city = form_class.cleaned_data['city']
        data.email = form_class.cleaned_data['email']
        data.state = form_class.cleaned_data['state']
        data.country = form_class.cleaned_data['country']
        data.zip = form_class.cleaned_data['zip_code']
        data.phone = form_class.cleaned_data['phone']
        data.user_id = current_user.id
        data.total = total
        data.ip = self.request.META.get('REMOTE_ADDR')
        ordercode = get_random_string(7).upper()
        data.code = ordercode
        user_mail = data.email
        print(user_mail)
        user_name = data.first_name
        print(ordercode)
        print(type(ordercode))
        data.save()
        bill['Name'] = data.first_name
        bill['Address'] = data.address
        bill['Order Code'] = ordercode

        print(bill)
        print(type(bill))

        shop_cart = ShopCart.objects.filter(user_id=current_user.id)
        total_cart = 0
        for rs in shop_cart:
            detail = OrderProduct()
            detail.order_id = data.id
            detail.product_id = rs.product_id
            detail.user_id = current_user.id
            detail.quantity = rs.quantity
            detail.price = rs.product.price
            detail.amount = rs.amount
            total_cart += rs.amount
            print(detail.amount)
            detail.save()

            # reduce quantity of sold product from amount of product
            product = Product.objects.get(id=rs.product_id)
            product.amount -= rs.quantity
            product.save()

        ShopCart.objects.filter(user_id=current_user.id).delete()
        self.request.session['cart_items'] = 0

        template_dir = os.path.join(os.path.dirname(__file__), 'templates')

        fileloader = jinja2.FileSystemLoader(template_dir)
        env = jinja2.Environment(loader=fileloader, autoescape=True)
        rendered = env.get_template('bill.html').render(shopcart=bill['Product'],
                                                        total=bill['Total'],
                                                        grand_total=bill['Grand Total(with GST)'],
                                                        ordercode=bill['Order Code'])
        filename = ordercode + '.html'
        output_file = ordercode + '.pdf'

        with open(f"{filename}", 'w') as f:
            f.write(rendered)

        send_mail_task.delay(ordercode, filename, user_mail, user_name, output_file)

        print('mail sent')

        return render(self.request, 'shop/order_completed.html', {'ordercode': ordercode, 'category': category})
