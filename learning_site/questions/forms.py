from django import forms
from .models import question,answer

class question_form (forms.ModelForm):
    class Meta :
        model = question
        fields = ('question','image')

class answer_form (forms.ModelForm):
     class Meta :
        model = answer
        fields = ('the_answer','image')
