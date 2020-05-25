from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int,
                                widget=forms.NumberInput(
                                    attrs={
                                    "placeholder":0,
                                    "min": 0,
                                    "id":"number",
                                    "class":"col-md-1 col-xs-1"
                                    }
                                ),
                                label=False
                                )
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
