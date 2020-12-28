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
        reciever = email #the email which is feeded into form
        topnews = request.POST.get('topnews')
        if topnews == "on":
            topnews = True
        else:
            topnews = False
        headlines = topnews

        wnews = request.POST.get('wnews')
        if wnews == "on":
            wnews = True
        else:
            wnews = False
        world = wnews
        
        bnews = request.POST.get('bnews')
        if bnews == "on":
            bnews = True
        else:
            bnews = False
        business = bnews

        snews = request.POST.get('snews')
        if snews == "on":
            snews = True
        else:
            snews = False
        sports = snews

        contact.name = name
        contact.email = email
        #contact.frequency = frequency
        contact.topnews = topnews
        contact.wnews = wnews
        contact.bnews = bnews
        contact.snews = snews
        contact.save()
        mailtest.main(reciever,headlines,world,business,sports)

        return HttpResponse("<h1>Thanks for subscribing</h1>")
    else:
        return render(request, 'news/subscription.html')
