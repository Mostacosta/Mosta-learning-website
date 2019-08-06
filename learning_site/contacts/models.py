from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=1,default="0")
    picture = models.ImageField(upload_to="profile_pic")
    my_course_no = models.CharField(max_length=2)
    
