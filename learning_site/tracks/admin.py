from django.contrib import admin
from .models import track,course,lesson,exam,exam_result
# Register your models here.

admin.site.register(track)
admin.site.register(course)
admin.site.register(lesson)
admin.site.register(exam)
admin.site.register(exam_result)