from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    
    return render(request , 'index.html')
    # return HttpResponse('done')

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact
from django.http import HttpResponseRedirect


from MyPortfolio.settings import *
def contact_view(request):
    print('run method')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', 'No Subject')
        message = request.POST.get('msg')

        if name and email and message:  # Basic validation
            # Save to database
            contact_msg = Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            contact_msg.save()

            # Send email
          
            subject=f"New Contact Message from {name}",
            message=f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}",
            fail_silently=False,       
            email_from = EMAIL_HOST_USER
            recipient_list = [email]  # Add recipient email addresses here
            try:
                send_mail(subject, message, email_from, recipient_list, fail_silently)
            except:
                pass    
            
            messages.success(request, "Your message has been sent successfully!")
            # Redirect with query parameter
            # return redirect('/contact/?scroll_to=contact')
            return HttpResponseRedirect('/#contact')

        else:
            messages.error(request, "All fields are required!")

    return render(request, 'contact.html')
