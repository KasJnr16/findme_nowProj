# forms.py
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title','name_of_item_finder', 'location_found','date_found','phone_number_of_item_finder','description']  # You can customize this list to include/exclude specific fields if needed
