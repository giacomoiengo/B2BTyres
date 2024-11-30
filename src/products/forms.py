from email.policy import default
from django import forms
from .models import Product

# filter_fields = ['brand', 'width', 'height']

def getBrandDistinctValues():
    return map(lambda o:(o.brand,o.brand), Product.objects.all().distinct('brand'))

def getWidthDistinctValues():
    return map(lambda o:(o.width,o.width), Product.objects.all().distinct('width'))

def getHeightDistinctValues():
    return map(lambda o:(o.height,o.height), Product.objects.all().distinct('height'))



class ProductFilterForm(forms.Form):
    brand  = forms.TypedMultipleChoiceField(required=True, empty_value=[],  coerce=str, help_text='Marca',     choices=getBrandDistinctValues)
    width  = forms.TypedMultipleChoiceField(required=False, empty_value=[], coerce=int, help_text='Larghezza', choices=getWidthDistinctValues)
    height = forms.TypedMultipleChoiceField(required=False, empty_value=[], coerce=int, help_text='Altezza',   choices=getHeightDistinctValues)