from django.db import models

# Create your models here. Inherit models.Model to be able to do it.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/')  # upload_to='' specify where to upload the image to.
    body = models.TextField()

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')