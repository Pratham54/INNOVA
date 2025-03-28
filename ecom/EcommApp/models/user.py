from django.db import models
from django.contrib.auth.hashers import make_password

class UserSignup(models.Model):
    full_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


    def register(self):
        self.save()

    @staticmethod
     
    def get_customer_by_email(email):
        try:
            return UserSignup.objects.get(email=email)
        except:
            return False
        
    def isExists(self):
        if UserSignup.objects.filter(email=self.email):
            return True
        
        return False