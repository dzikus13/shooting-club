from django.shortcuts import render


def base(request):
    return render(request, "manager/index.html")