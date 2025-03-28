from django.db import models


class Services(models.Model):
    name=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
    image=models.ImageField(upload_to="Services_Images")