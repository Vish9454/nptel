from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    home1 = Home()
    home1.name = "Vishal Singh"
    home1.fblink = 'https://www.facebook.com/vish2222'
    home1.gmail = 'mailto: vish9454@gmail.com?subject=Resume Testing&body=Hi Vishal, It is Testing'

    about1 = AboutMe1()
    about1.img = 'vishal.jpg'
    about1.description = "Seeking a challenging opportunity in a dynamic environment where innovation, education and " \
                         "sense of ownership are valued and encouraged. Goal oriented,highly motivated with a strong " \
                         "orientation to put my best into the job allocated.Ability to gel with people and work in a " \
                         "team. Confident and poised in interactions with individuals of all levels. Very curious to " \
                         "know things. Charismatic personality. Respects seniors and good helping nature. Interested " \
                         "in growth of company. "

    about2 = AboutMe2()
    about2.name = "Vishal Singh"
    about2.age = 27
    about2.exp = 2
    about2.country = "India"
    about2.location = "Gurugram"
    about2.email = "vish9454@gmail.com"
    about2.phone = "+91 9205725487"




    return render(request, "index.html", {'home1': home1,'about1': about1 , 'about2': about2})
