from django.shortcuts import render


def index(request):
    return render(request, "manager/index.html")


def about(request):
    return render(request, "manager/about.html")


def contact(request):
    return render(request, "manager/contact.html")


def home(request):
    return render(request, "manager/home.html")


def pages(request):
    return render(request, "manager/pages.html")


def services(request):
    return render(request, "manager/services.html")