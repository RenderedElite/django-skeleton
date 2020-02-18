from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactUs
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')
	
def pricing(request):
	return render(request, 'pricing.html')

def contact(request):
	form = ContactUs()
	if request.method == 'POST':
		form = ContactUs(request.POST)
		if form.is_valid():
			sender_name = form.cleaned_data['name']
			sender_email = form.cleaned_data['email']
			message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
			send_mail('New Enquiry', message, sender_email, ['sendto@example.com'])
			return HttpResponse('Thanks for contacting us!')		
		else:
			form = ContactUs()
	return render(request, 'contact.html', {'form':form})


