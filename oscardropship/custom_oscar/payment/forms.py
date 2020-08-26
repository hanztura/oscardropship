from oscar.apps.payment.forms import *
from django import forms

from .models import PaypalOrder


class PaypalOrderModelForm(forms.ModelForm):
    class Meta:
        model = PaypalOrder
        fields = ('details', 'order_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['details'].required = True
        self.fields['order_id'].required = True
