from django import forms

class ThingForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.CharField(widget=forms.NumberInput)