from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=1,default="0")
    picture = models.ImageField(upload_to="profile_pic")

    def __str__(self):
        return self.user.username

class teacher (models.Model):
    name = models.CharField(max_length=100)
    position  = models.CharField(max_length=100)
    bio = models.TextField()
    fb = models.CharField(max_length=200) 
    ldn = models.CharField(max_length=200) 
    tw = models.CharField(max_length=200) 
    img = models.ImageField(upload_to="teachers",null=True)

    def __str__(self):
        return self.name
        
       
