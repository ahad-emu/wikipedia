from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    name = forms.CharField()
    defination = forms.CharField()
    details = forms.CharField()

    class Meta:
        model = Item
        fields = ["name", "defination", "details"]
