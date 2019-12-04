from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tracks.api.serializers import track_serializer,course_serializer,lesson_serializer,exam_serializer
from ..models import track,course,lesson,exam,exam_result
from rest_framework import generics
from datetime import datetime
import dateutil.parser
from django.utils import timezone
from rest_framework.parsers import JSONParser


class all_list (generics.ListAPIView):

    def get_queryset(self):
        queryset = ''
        if self.kwargs['which'] =='track':
            queryset = track.objects.all()
        elif self.kwargs['which'] == 'course':
            queryset = course.objects.all()
        else :
            queryset = lesson.objects.all()
        return queryset

    def get_serializer_class (self):
        serializer_class = ''
        if self.kwargs['which'] =='track':
            serializer_class = track_serializer
        elif self.kwargs['which'] == 'course':
            serializer_class = course_serializer
        else :
            serializer_class = lesson_serializer
        return serializer_class

class exam_api (APIView):
    def get(self, request,course_name,format=None):
        course_ = course.objects.get(name=course_name)
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
                return Response ("comeback after"+ str(hours))

        questions = exam.objects.filter(course=course_)
        serializer = exam_serializer(questions,many=True)
        request.session['time'] = datetime.now().isoformat()
        return Response (serializer.data)
    
    def post(self, request,course_name ,format=None):
        course_ = course.objects.get(name=course_name)
        try:
            result = exam_result.objects.get(course=course_,user=request.user)
        except :
            result = None 
        serializer = exam_serializer(data=request.data,many=True)
        if serializer.is_valid():
            print(serializer.data)
        else:
            return Response(serializer.errors)
        time_ = request.session.get('time')
        past_time = dateutil.parser.parse(time_)
        now_time = datetime.now()
        dif = now_time-past_time
        dif = dif.total_seconds()
        if dif is not None and dif<1800:
            score = 0
            for question in serializer.data:
                question_ = exam.objects.get(name=question["name"])
                if question_.right_answer == question.get("right_answer"):
                    score +=1
            precentage = (score/len(serializer.data)) * 100
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
                return Response ("you succed")
            else :
                if result:
                    result.case = 'failed'
                    result.times +=1
                    result.date = timezone.now()
                    result.degree=precentage
                else:
                    result =exam_result(user=request.user,course=course_,case='failed',degree=precentage)
                result.save()
                return Response ("you failed")
        else:
            return Response ("no session")
        
        

        
       
        
               
    
    
