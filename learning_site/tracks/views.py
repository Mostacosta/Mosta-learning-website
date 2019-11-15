from django.shortcuts import render
from django.http import HttpResponse
from .models import track,course,lesson,exam,exam_result
from questions.models import question ,answer
from questions.forms import question_form
from datetime import datetime
import dateutil.parser
from django.utils import timezone

# Create your views here.
def track_list(request):
    tracks = track.objects.all()
    return render (request,'tracks/track_list.html',{"tracks":tracks})

def course_list(request,pk):
    my_track = track.objects.get(pk=pk)
    courses = course.objects.filter(track=my_track)
    return render (request,'tracks/course_list.html',{"courses":courses,"track":my_track})

def lesson_list(request,pk):
    my_course = course.objects.get(pk=pk)
    lessons = lesson.objects.filter(course=my_course)
    return render (request,'tracks/lesson_list.html',{"lessons":lessons,"course":my_course.name})

def lesson_view (request,pk):
    form = question_form()
    lesson_ = lesson.objects.get(pk=pk)
    lessons_ = lesson.objects.filter(course=lesson_.course)
    questions = question.objects.filter(lesson=lesson_)
    answers = []
    for question_ in questions :
        answers.append(answer.objects.filter(question=question_))
    zip_list = zip (questions,answers)
    if request.user not in lesson_.watching_users.all():
        lesson_.watching_users.add(request.user)
        lesson_.save()
    return render (request,'tracks/lesson.html',{"lesson":lesson_,'zip':zip_list,"form":form,"lessons":lessons_})

def exam_view (request,pk):
    course_ = course.objects.get(pk=pk)
    questions = exam.objects.filter(course=course_)
    try:
        result = exam_result.objects.get(course=course_,user=request.user)
    except :
        result = None
    if result :
        last_time = result.date
        last_time = last_time.replace(tzinfo=None)
        dif = datetime.now()-last_time
        dif = dif.total_seconds()
        expire_date = 259200*result.times
        hours = expire_date//(60*60)
        if dif < expire_date:
            return HttpResponse ("comeback after"+str(hours))
    if request.method == "POST":
        if request.session.get('time'):
            time_ = request.session.get('time')
            past_time = dateutil.parser.parse(time_)
            now_time = datetime.now()
            dif = now_time-past_time
            dif = dif.total_seconds()
        if dif is not None and dif<1800:
            score = 0
            for question in questions:
                if question.right_answer == request.POST[question.name]:
                    score +=1
            precentage = (score/len(questions)) * 100
            if precentage > 50 :
                if request.user not in course_. succeeded_users.all():
                    course_. succeeded_users.add(request.user)
                    course_.save()
                if result:
                    result.case = 'success'
                    result.times =1
                    result.date = timezone.now()
                    result.degree=precentage
                else:
                    result =exam_result(user=request.user,course=course_,case='success',degree=precentage)
                result.save()
                return HttpResponse ("you succed")
            else :
                if result:
                    result.case = 'failed'
                    result.times +=1
                    result.date = timezone.now()
                    result.degree=precentage
                else:
                    result =exam_result(user=request.user,course=course_,case='failed',degree=precentage)
                result.save()
                return HttpResponse ("you failed")
        else:
            return HttpResponse ("no session")
    else:
        request.session['time'] = datetime.now().isoformat()
    return render (request,'tracks/exam.html',{"questions":questions})






