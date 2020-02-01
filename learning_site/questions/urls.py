from django.urls import path
from .views import question_view,question_list,answer_view,answer_list,answer_like,lesson_view
from django.conf.urls import url

app_name = 'questions'

urlpatterns = [
   path('view/<int:pk>',question_view,name='question_view'),
   path('list/<int:pk>',question_list,name='question_list'),
   path('answer/<int:pk>',answer_view,name='answer_view'),
   path('anslist/<int:pk>',answer_list,name='answer_list'),
   path('like/<int:pk>',answer_like,name='like'),
   path('/lesson_details/<int:pk>',lesson_view,name='lesson_view'),
   
]