from django.shortcuts import render,get_object_or_404
from .models import Qu
import random

def home(request):
    return render(request,'randq/home.html')

def randquote(request):
    quotes=Qu.objects.all()
    randquotes=random.choice(quotes)
    return render(request,'randq/quotes.html',{'quotes':randquotes})