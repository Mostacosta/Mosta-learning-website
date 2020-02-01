from django.urls import path
from .views import  track_list,lesson_list,course_list,lesson_view,exam_view,lesson_watch

app_name = 'tracks'

urlpatterns = [
  path('',track_list,name = 'track_list'),
  path('/course/<int:pk>',course_list,name = 'course_list'),
  path('/lesson/<int:pk>',lesson_list,name = 'lesson_list'),
  path('/exam/<int:pk>',exam_view,name='exam_view'),
   path('/lessonwatch/<int:pk>',lesson_watch,name='lesson_watch')

]