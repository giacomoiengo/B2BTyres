from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(label='Pezzi',required=True, min_value=1, initial=1)

    
    