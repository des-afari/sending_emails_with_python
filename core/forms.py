from django import forms
from .models import Recipient


class RecipientForm(forms.ModelForm):    
    class Meta:
        model = Recipient
        fields = '__all__'


class EmailForm(forms.Form):
    sender = forms.EmailField(widget=forms.TextInput(attrs={'value': 'afaridesmond@gmail.com', 'type': 'email', 'placeholder': 'From'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type email here...'}))


