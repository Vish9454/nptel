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

    whatiknow1 = WhatIknow()
    whatiknow1.tab = "Python"
    whatiknow1.content = "Functions and OOPS related programming." \
                         "<br /> Global and Globals,Recursions,Lambda function,Decorators,constructors,getters and setters." \
                         "<br /> Concepts like inner classes ,defunctions under functions. Inheritance and its types(MRO).Constructors in inheritance. " \
                         "<br /> Polymorphism and its types-(Duck typing,Operator Overloading,Method Overloading,Method overridding)" \
                         "<br /> Abstract classes and methods in python." \
                         "<br /> Generators and Iterators in Python Numpy in python." \
                         "<br /> Packages in python for array as numpy and its types." \
                         "<br /> File Handling in python. Multithreading in python." \
                         "<br /> Data frames concept Data Science related skills like Pandas,Matrix,Matplotlib.pylab." \
                         "<br /> The Scatter plot,Bar plot,Histogram ,Box and Whiskers plot,Pairwise plot." \
                         "<br /> Dealing with missing data in dataframe. Matimatical conceptsas Matrices, correlation (pearsons,spearman, kendall’s rank) ,probability. " \
                         "<br /> Patterns in python."
    whatiknow2 = WhatIknow()
    whatiknow2.tab = "Linux"
    whatiknow2.content = "<li>How to install and server setup Linux</li>" \
                         "<li>Manage local Linux users and Groups and there password mechanism</li>" \
                         "<li>Control access to files with Linux file system permission-Security reasons</li>" \
                         "<li>Moniter and manage Linux processes.Control services and deamons</li>" \
                         "<li>Accessing Linux file systems-access and inspect file system</li>" \
                         "<li>Installing and using Virtualized systems.</li>" \
                         "<li>Create and edit files with vim.Process Management by top, ps and Use regular expressions with grep</li>" \
                         "<li>Creating YUM Repository and installing Packages via YUM</li>" \
                         "<li>Zip ans Unzipping of a file and usage of Tar</li>" \
                         "<li>Bash Scripting(Shell Programming ,KSH horn Shell ,BASH-Bourne Again Shell)</li>" \
                         "<li>Usage of Cron for Scheduling jobs</li>" \
                         "<li>SELinux (Permission, Disabled, Enforcing)</li>" \
                         "<li>LVM(Logical Volume Management)</li>"

    education_btech = Education()
    education_btech.qualify_name = 'B.TECH , JSS (Noida)'
    education_btech.qualify_yr = '2013 - 2017'
    education_btech.qualify_board = 'From UPTU board'
    education_btech.qualify_percent = 'Got Agrregate percentage of 72% in graduation'

    education_class12 = Education()
    education_class12.qualify_name = 'Holy Cross School, Ballia'
    education_class12.qualify_yr = '2010 - 2012'
    education_class12.qualify_percent = 'Got Agrregate percentage of 79% in Class 12'
    education_class12.qualify_board = 'From ICSE Board'

    education_class10 = Education()
    education_class10.qualify_name = 'Holy Cross School, Ballia'
    education_class10.qualify_yr = '2008 - 2010'
    education_class10.qualify_percent = 'From ICSE Board'
    education_class10.qualify_board = 'Got Agrregate percentage of 86% in Class 10'

    experience = Experience()
    experience.designation = 'In Ameyo Soft Solutions as Product Engineer'
    experience.exp_count = 'Octobar 2018 - Present'
    experience.work_in_exp = "<li>Proved worth in many projects with clients such as OLX ,Byjus ,Bluecloud ,Lovely Professional University(LPU),Finnew Pvt Ltd ,Petroleum University,Myntra,India bulls,Equitas bank,Magic Bricks, Royal Bank of Scotland and many more.</li>" \
                             "<li>Have made bash scripts for clients to make work easier and also gave helping hand in debugging for services modules.</li>" \
                             "<li>Embraced with basics of Applications testing and and its usage.</li>" \
                             "<li>A sense of urgency ,commitment and focus on the right priorities to develop solutions on timely basis.</li>" \
                             "<li>An effective communicator with technical ,reasoning and analytical skills.</li>" \
                             "<li>Setting the server up frm scratch to finally handing it to client .</li>"
    education = [education_btech, education_class12, education_class10]

    whatiknow = [whatiknow1, whatiknow2]

    return render(request, "index.html",
                  {'home1': home1, 'about1': about1, 'about2': about2, 'whatiknow': whatiknow, 'education': education,
                   'experience': experience})
