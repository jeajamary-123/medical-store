from django import forms
from .models import med_kit

class ProductForm(forms.ModelForm):
    class Meta:
        model = med_kit
        fields = ['Medname','Description','Price','Quantity']
class MedicineSearchForm(forms.Form):
    search_query = forms.CharField(label='Search Medicine', max_length=100)