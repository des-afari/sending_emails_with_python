from django import forms


class EmailForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type here...'}))