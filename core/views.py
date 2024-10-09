from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *

class HomePageView(TemplateView):
    template_name = 'homePage.html'
