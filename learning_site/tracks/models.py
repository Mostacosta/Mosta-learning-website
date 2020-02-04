from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from contacts.models import teacher

# Create your models here.
class track(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField()
    image = models.ImageField(blank=True,upload_to="tracks")
    points = models.TextField(blank=True)
    track_designer = models.ForeignKey(teacher,on_delete=models.SET_NULL,null=True)


    def __str__ (self):
        return self.name

class course (models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField()
    order = models.IntegerField(max_length=5)
    track = models.ManyToManyField(track)
    succeeded_users = models.ManyToManyField(User,blank=True)

    def __str__ (self):
        return self.name

class lesson (models.Model):
    name = models.CharField(max_length=150)
    link = models.URLField()
    order = models.IntegerField(max_length=5)
    course = models.ForeignKey(course,on_delete=models.CASCADE)
    watching_users = models.ManyToManyField(User,blank=True)

    def __str__ (self):
        return self.name

class exam (models.Model):
    name = models.CharField(max_length=150)
    question = models.CharField(max_length=200)
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100)
    answer4 = models.CharField(max_length=100)
    choices = (("answer1",'answer1'),("answer2",'answer2'),("answer3",'answer3'),("answer4",'answer4'))
    right_answer = models.CharField(max_length=20,choices=choices,null = True,blank = True)
    course = models.ForeignKey(course, on_delete=models.CASCADE)

    def __str__ (self):
        return self.name


class exam_result (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    choices = (("failed",'failed'),("success",'success'))
    case = models.CharField(max_length=20,choices=choices,default="failed")
    times = models.IntegerField(default=1)
    date = models.DateTimeField(default=timezone.now)
    degree = models.FloatField(null=True)

    def __str__(self):
        return self.course.name

