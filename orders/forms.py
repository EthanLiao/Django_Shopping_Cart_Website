# -*- coding: UTF-8 -*-
from django import forms

from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Div,Field
from django.core.exceptions import ValidationError
import calendar
import re
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]
# TRANS_CHOICES = [(1,'貨到付款'),(2,'匯款')]
TRANS_CHOICES = [(1,'貨到付款')]
class OrderCreateForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        # make city field as the div and id is "twzipcode_ADV"
        self.helper = FormHelper()
        self.helper = Layout(
            Div(Field('city') , id="twzipcode_ADV"),
        )
        self.fields['first_name'].widget = forms.TextInput(attrs={
                'class': 'fname_input',
                })
        self.fields['last_name'].widget = forms.TextInput(attrs={
                'class': 'lname_input',
                })
        self.fields['email'].widget = forms.TextInput(attrs={
                'class': 'email_input',
                'id': 'email_input_id',
                'onblur' : 'validate'
                })
        self.fields['phone_num'].widget = forms.TextInput(attrs={
                'class': 'phone_input',
                })
        self.fields['address'].widget = forms.TextInput(attrs={
                'class': 'address_input',
                'id' : 'address_input_id'
                })
        self.fields['transportationMethod'] = forms.ChoiceField(choices=TRANS_CHOICES)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not re.match(EMAIL_REGEX, email):
            raise forms.ValidationError('Invalid email format')

        return email
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_num'
        ,'city','address','transportationMethod']
