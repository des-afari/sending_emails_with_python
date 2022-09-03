from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import EmailForm, RecipientForm
from .models import Recipient


# Create your views here.
def index(request):
    if request.method == 'POST' and 'submit-email-address' in request.POST:
        recipient = RecipientForm(request.POST)

        if recipient.is_valid():
            if Recipient.objects.filter(email=request.POST['email']).exists():
                messages.info(request, "Email already listed")
                return redirect('index')

            else:
                recipient.save()
                return redirect('index')

        else:
            messages.info(request, "Invalid email address")
            return redirect('index')
        

    elif request.method == "POST" and 'send-email' in request.POST:
        emailForm = EmailForm(request.POST)

        if emailForm.is_valid():
            return redirect('index')
    

    else:
        recipients = Recipient.objects.all()
        emailForm = EmailForm()
        recipientForm = RecipientForm()
        
        context = {
            'recipients': recipients,
            'emailForm': emailForm,
            'recipientForm': recipientForm
        }

        return render(request, 'index.html', context)


def delete_item(request, pk):
    del_recipient = Recipient.objects.get(id=pk)
    del_recipient.delete()
    return redirect('index')
    
