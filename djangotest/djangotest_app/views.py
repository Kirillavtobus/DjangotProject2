from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'home.html')


def page_2(request):
    return render(request, 'page_2.html')

