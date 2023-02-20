from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from stripe_buy.forms import OrderForm
from stripe_buy.models import Item, Order
from stripe_buy.settings import STRIPE_KEY, PAY_REDIRECT_URL
import stripe
import json

class IndexView(TemplateView):

    template_name = 'index.html'

class ItemView(View):

    def get(self, request, *agrs, **kwargs):

        item = Item.objects.get(id=kwargs['pk'])
        return render(
            request,
            'item.html',
            context={
            'item': item
            }
        )

class BuyItemView(View):

    def get(self, request, *agrs, **kwargs):

        item = Item.objects.get(pk=kwargs['pk'])
        stripe.api_key = STRIPE_KEY
        session = stripe.checkout.Session.create(
            line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
            'unit_amount_decimal': item.price,
            },
            'quantity': 1,
            }],
            mode='payment',
            success_url=PAY_REDIRECT_URL,
            cancel_url=PAY_REDIRECT_URL,
        )
        data = json.dumps(session)
        return HttpResponse(data, content_type='application/json')

class OrderView(View):

    def get(self, request, *agrs, **kwargs):

        order = Order.objects.get(id=kwargs['pk'])
        return render(
            request,
            'order.html',
            context={
            'order': order
            }
        )


class OrderBuyView(View):

    def get(self, request, *agrs, **kwargs):

        order = Order.objects.get(pk=kwargs['pk'])
        stripe.api_key = STRIPE_KEY
        order_items = order.items.all()
        coupon = None
        tax_rates = []
        if order.discount:
            try:
                coupon = stripe.Coupon.retrieve(order.discount.dis_id)
            except stripe.error.InvalidRequestError:
                coupon = stripe.Coupon.create(
                        duration=order.discount.duration,
                        id=order.discount.dis_id,
                        percent_off=order.discount.percent_off
                    )
            for tax in order.taxes.all():
                tax_rate = stripe.TaxRate.create(
                    display_name=tax.display_name,
                    percentage=tax.percentage,
                    inclusive=tax.inclusive,
                    )
                tax_rates.append(tax_rate.id)
        stripe_line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
            'unit_amount': item.price,
            },
            'quantity': 1,
            'tax_rates': tax_rates
            } for item in order_items]
        session = stripe.checkout.Session.create(
            line_items=stripe_line_items,
            mode='payment',
            discounts=[{
                'coupon': coupon.id,}] if coupon else None,
            success_url=PAY_REDIRECT_URL,
            cancel_url=PAY_REDIRECT_URL,
        )
        data = json.dumps(session)
        return HttpResponse(data, content_type='application/json')

class ItemListView(ListView):

    model = Item
    template_name = 'list.html'
    context_object_name = 'items'
    extra_context = {
        'title': 'Товары',
        'link': 'get_item'
    }

class OrderCreateView(CreateView):

    model = Order
    form_class = OrderForm
    template_name = 'order_create.html'
    success_url = reverse_lazy('orders_list')

class OrdersListView(ListView):

    model = Order
    template_name = 'list.html'
    context_object_name = 'items'
    extra_context = {
        'title': 'Заказы',
        'link': 'get_order'
    }
