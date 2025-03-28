from django.db import models


class Projects(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="Projects_Images")