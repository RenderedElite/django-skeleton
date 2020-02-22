from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')
	
def pricing(request):
	return render(request, 'pricing.html')



