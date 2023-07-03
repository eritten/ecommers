from django.shortcuts import render
from .models import Product, Address, AddToCard
from django.contrib.auth.models import User
from django.core,mail import send_mail
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def home(request):
    return render(request, 'home.html')

