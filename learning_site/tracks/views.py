from django.shortcuts import render
from .models import track,course,lesson,exam

# Create your views here.
def track_list(request):
    tracks = track.objects.all()
    return render (request,'tracks/track_list.html',{"tracks":tracks})

def course_list(request,pk):
    my_track = track.objects.get(pk=pk)
    courses = course.objects.filter(track=my_track)
    return render (request,'tracks/course_list.html',{"courses":courses})

def lesson_list(request,pk):
    my_course = course.objects.get(pk=pk)
    lessons = lesson.objects.filter(course=my_course)
    return render (request,'tracks/lesson_list.html',{"lessons":lessons})





