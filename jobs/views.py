from django.shortcuts import render

# Create your views here.
def uyi(request):
    return render(request, 'jobs/home.html')