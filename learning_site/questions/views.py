from django.shortcuts import render,redirect
from tracks.models import lesson
from .models import question,answer
from .forms import question_form,answer_form
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
            return redirect('questions:question_list',pk=pk)
    else:
        return render (request,'questions/ask.html',{'form':form})

def question_list(request,pk):
    questions = question.objects.filter(lesson=lesson.objects.get(pk=pk))
    return render(request,'questions/question_list.html',{'questions':questions})


def answer_view(request,pk):
        form = answer_form()
        if request.method == "POST":
                form = answer_form(request.POST)
                if form.is_valid():
                        new_answer = form.save(commit=False)
                        new_answer.question = question.objects.get(pk=pk)
                        new_answer.user = request.user
                        new_answer.save()
                        return redirect('questions:answer_list',pk=pk)
        else:
                return render (request,'questions/answer.html',{'form':form})

def answer_list (request,pk):
        answers = answer.objects.filter(question=question.objects.get(pk=pk))
        return render(request,'questions/answer_list.html',{'answers':answers})

def answer_like (request,pk):
        the_answer = answer.objects.get(pk=pk)
        user = request.user
        if user in the_answer.likes.all() :
                the_answer.likes.remove(user)
        else:
                the_answer.likes.add(user)
        return redirect ('questions:answer_list',pk=the_answer.question.pk)



