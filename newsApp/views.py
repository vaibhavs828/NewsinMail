from django.shortcuts import render
from django.http import HttpResponse
from newsApp.models import Contact
from newsApp import mailtest
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request):
    # return HttpResponse("This is homepage")
    return render(request, 'news/index.html')


def subscription(request):
    # return HttpResponse("huhuhu")
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        frequency = request.POST.get('frequency')
        contact.name = name
        contact.email = email
        contact.frequency = frequency
        contact.save()
        mailtest.main()
        return HttpResponse("<h1>Thanks for subscribing</h1>")

    return render(request, 'news/subscription.html')
