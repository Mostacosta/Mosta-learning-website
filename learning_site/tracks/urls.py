from django.urls import path
from .views import  track_list,lesson_list,course_list,lesson_view,exam_view

app_name = 'tracks'

urlpatterns = [
  path('',track_list,name = 'track_list'),
  path('/course/<int:pk>',course_list,name = 'course_list'),
  path('/lesson/<int:pk>',lesson_list,name = 'lesson_list'),
  path('/lesson_details/<int:pk>',lesson_view,name='lesson_view'),
  path('/exam/<int:pk>',exam_view,name='exam_view'),

]