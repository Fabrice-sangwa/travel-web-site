

from django.shortcuts import render
from datetime import datetime


# Create your views here.

def welcome(request):
    return render(request, "welcome/index.html", context={"date": datetime.today()})
