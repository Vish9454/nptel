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


class TabCount:
    tabcount: int


class WhatIknow:
    tab: str
    content: str


class Education:
    qualify_name: str
    qualify_yr: str
    qualify_percent: str
    qualify_board = str


class Experience:
    designation: str
    exp_count: str
    work_in_exp: str
