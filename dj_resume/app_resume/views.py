from django.shortcuts import render
from .models import *

home = Home('Vishal', "","");
aboutMe = AboutMe("","")
data = Data(home, aboutMe);



# Create your views here.
def index(request):
    return render(request, "index.html", data)
