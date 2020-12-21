from django.urls import path,include
from newsApp import views

urlpatterns = [
    path("", views.index, name = "Home"),
    path("subscription/", views.subscription, name = "Subscription"),
]
