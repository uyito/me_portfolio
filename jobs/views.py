from django.shortcuts import render
from .models import Job
from .models import AboutMe


# Create your views here.
def uyi(request):
    jobs = Job.objects
    about_me = AboutMe.objects
    return render(request, 'jobs/home.html', {'jobs': jobs, 'about_me': about_me})

