from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


class AboutMe(models.Model):
    about = models.CharField(max_length=300)