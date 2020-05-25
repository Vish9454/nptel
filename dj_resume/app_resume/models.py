from django.db import models


# Create your models here.
class Home:
    name: str
    fblink: str
    gmail: str


class AboutMe1:
    img: str
    description: str


class AboutMe2:
    name: str
    age: float
    experience: float
    country: str
    location: str
    email: str
    phone: str
