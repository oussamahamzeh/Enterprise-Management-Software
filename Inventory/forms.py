from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'company', 'category', 'quantity', 'purchase_cost', 'shipping_cost', 'selling_price', 'description','rebuy_till','code']
