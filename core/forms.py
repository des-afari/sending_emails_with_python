from django import forms
from .models import Recipient


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = '__all__'


class EmailForm(forms.Form):
    sender = forms.EmailField(widget=forms.TextInput(attrs={'value': 'afaridesmond@gmail.com'}))
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type here...'}))


