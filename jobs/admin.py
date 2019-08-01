from django.contrib import admin
from .models import Job
from .models import AboutMe

# Register your models here.
admin.site.register(Job)
admin.site.register(AboutMe)