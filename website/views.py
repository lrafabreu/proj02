import os
from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, "home.html", {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
		api = ""
		try:
			send_mail(
			message_name,
			message,
			os.environ.get('EMAIL_HOST_USER'),
			[message_email, 'lrafabreu@gmail.com'],
			fail_silently=False,
			)
		except Exception as e:
			api = "Error..."
		return render(request, "contact.html", {'api': api})
	else:
		return render(request, "contact.html", {})

