from django.urls import path
from .views import  track_list,lesson_list,course_list

app_name = 'tracks'

urlpatterns = [
  path('',track_list,name = 'track_list'),
  path('/course/<int:pk>',course_list,name = 'course_list'),
  path('/lesson/<int:pk>',lesson_list,name = 'lesson_list'),

]