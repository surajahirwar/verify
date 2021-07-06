from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



class Adduserdata(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    admission_no = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'pyimage', default="")


    def __str__(self): 

        return self.name + " "  + "by"   + self.admission_no

