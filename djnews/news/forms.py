from django import forms

class ApikeyForm(forms.Form):
    apikey=forms.CharField(label='apikey', max_length=100)
