from django.db import models

# Create your models here. Inherit models.Model to be able to do it.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')  # upload_to='' specify where to upload the image to, INSIDE THE MEDIA FOLDER.
    summary = models.CharField(max_length=200)
