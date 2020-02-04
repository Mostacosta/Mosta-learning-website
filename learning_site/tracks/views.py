from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import track,course,lesson,exam,exam_result
from questions.models import question ,answer
from questions.forms import question_form
from datetime import datetime
import dateutil.parser
from django.utils import timezone
from django.views.decorators.cache import cache_page
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def track_list(request):
    tracks = track.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(tracks, 3)
    try:
        tracks = paginator.page(page)
    except PageNotAnInteger:
        tracks = paginator.page(1)
    except EmptyPage:
        tracks = paginator.page(paginator.num_pages)

    return render (request,'tracks/track-list.html',{"tracks":tracks})

def course_list(request,pk):
    my_track = track.objects.get(pk=pk)
    courses = course.objects.filter(track=my_track).order_by("order")
    points = my_track.points.split(",")
    lessons_ = []
    for course_ in courses:
        lessons = lesson.objects.filter(course=course_)
        lessons_.append(lessons)
    zip_ = zip(courses,lessons_)
    if request.user.is_authenticated:
        pass
    else:
        messages.error(request,"login to be able to preview lessons")
    return render (request,'tracks/course-details.html',{"courses":zip_,"track":my_track,"len":len(courses),"points":points})

def lesson_list(request,pk):
    my_course = course.objects.get(pk=pk)
    lessons = lesson.objects.filter(course=my_course)
    return render (request,'tracks/lesson_list.html',{"lessons":lessons,"course":my_course.name})

def lesson_view (request,pk):
    form = question_form()
    lesson_ = lesson.objects.get(pk=pk)
    if request.method == "POST":
        form = question_form(request.POST,request.FILES)
        if form.is_valid():
            ques_=form.save(commit=False)
            ques_.user = request.user
            ques_.lesson=lesson_
            form.save()
    questions = question.objects.filter(lesson=lesson_)
    answers = []
    for question_ in questions :
        answers.append(answer.objects.filter(question=question_))
    zip_list = zip (questions,answers)
    return render (request,"questions/answer_list.html",{"zip":zip_list,"form":form})

def lesson_watch (request,pk):
    lesson_ = lesson.objects.get(pk=pk)
    if request.user not in lesson_.watching_users.all():
        lesson_.watching_users.add(request.user)
        lesson_.save()
    return HttpResponse("watched")

@login_required(redirect_field_name="contacts:signup")
@cache_page(60)
def exam_view (request,pk):
    course_ = course.objects.get(pk=pk)
    questions = sorted(exam.objects.filter(course=course_),key=lambda x: random.random()) 
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
    print(request.session['time'])
    return render (request,'tracks/exam.html',{"questions":questions})






