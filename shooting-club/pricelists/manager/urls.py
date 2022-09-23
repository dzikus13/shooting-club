from django.contrib import admin
from django.urls import path
from .views import index, about, contact, home, pages, services
from . import views

urlpatterns = [
    path("", index),
    path("about", about),
    path("contact", contact),
    path("home", home),
    path("pages", pages),
    path("services", services)
]