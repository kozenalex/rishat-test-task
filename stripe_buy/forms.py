from django import forms
from stripe_buy.models import Order

class OrderForm(forms.ModelForm):

    class Meta:

        model = Order
        fields =['items', 'discount', 'taxes']