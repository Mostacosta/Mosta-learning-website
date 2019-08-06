from django.db import models

# Create your models here.
class track(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField()

class course (models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField()
    order = models.IntegerField(max_length=5)
    track = models.ForeignKey(track,on_delete=models.CASCADE)

class lesson (models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField()
    order = models.IntegerField(max_length=5)
    course = models.ForeignKey(course,on_delete=models.CASCADE)

class exam (models.Model):
    name = models.CharField(max_length=150)
    question = models.CharField(max_length=200)
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100)
    answer4 = models.CharField(max_length=100)
    choices = ((answer1,'answer1'),(answer2,'answer2'),(answer3,'answer3'),(answer4,'answer4'),)
    right_answer = models.CharField(max_length=20,choices=choices)
    course = models.ForeignKey(course, on_delete=models.CASCADE)
