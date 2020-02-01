from django.shortcuts import render,redirect,HttpResponse
from tracks.models import lesson
from .models import question,answer
from .forms import question_form,answer_form
from django.http import JsonResponse
from django.core import serializers
from django.template.loader import render_to_string
from permissions.permissions import active_user_required
from django.contrib.auth.decorators import login_required
# Create your views here.

def question_view (request,pk):
    form = question_form()
    if request.method == 'POST':
        form = question_form(request.POST)
        if form.is_valid():
            new_question = form.save(commit= False)
            new_question.lesson = lesson.objects.get(pk=pk)
            new_question.user = request.user
            new_question.save()
            return redirect('tracks:lesson_view',pk=pk)
    else:
        return redirect('tracks:lesson_view',pk=pk)

def question_list(request,pk):
    questions = question.objects.filter(lesson=lesson.objects.get(pk=pk))
    return render(request,'questions/question_list.html',{'questions':questions})


def answer_view(request,pk):
        form = answer_form()
        question_ = question.objects.get(pk=pk)
        if request.method == "POST":
                form = answer_form(request.POST)
                if form.is_valid():
                        new_answer = form.save(commit=False)
                        new_answer.question = question_
                        new_answer.user = request.user
                        new_answer.save()
                else:
                        print(form.errors)
        return redirect('questions:lesson_view',pk=question_.lesson.pk)

     
def answer_list (request,pk):
        question_ = question.objects.get(pk=pk)
        answers = answer.objects.filter(question= question_)
        form = answer_form()
        if request.method == "POST":
                form = answer_form(request.POST)
                if form.is_valid():
                        new_answer = form.save(commit=False)
                        new_answer.question = question_
                        new_answer.user = request.user
                        new_answer.save()
        return render(request,'questions/answer_list.html',{'answers':answers,"question":question_,"form":form})

def answer_like (request,pk):
        the_answer = answer.objects.get(pk=pk)
        user = request.user
        if user in the_answer.likes.all() :
                the_answer.likes.remove(user)
        else:
                the_answer.likes.add(user)
        return HttpResponse("a7a")


@login_required(redirect_field_name="contacts:signup")
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
            return redirect('questions:lesson_view',pk=pk)
    questions = question.objects.filter(lesson=lesson_)
    answers = []
    for question_ in questions :
        answers.append(answer.objects.filter(question=question_))
    zip_list = zip (questions,answers)
    return render (request,"questions/answer_list.html",{"zip":zip_list,"form":form})