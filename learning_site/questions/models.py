from django.db import models
from tracks.models import lesson
from django.contrib.auth.models import User

# Create your models here.
class question (models.Model):
    question = models.TextField()
    image = models.ImageField(upload_to="questions",blank = True)
    lesson = models.ForeignKey(lesson,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class answer(models.Model):
    the_answer = models.TextField()
    image = models.ImageField(upload_to="answers",blank = True)
    question = models.ForeignKey(question,on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name='user_likes',blank=True)
    
