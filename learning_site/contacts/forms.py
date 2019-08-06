from django import forms
from django.contrib.auth.models import User
from .models import profile

class user_form (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model = User
        fields = ('password','username' ,'email')

class profile_form (forms.ModelForm):
    class Meta :
        model = profile
        fields = ('picture',)


class reset_password_mail (forms.ModelForm):
    class Meta :
        model = User
        fields = ('email',)

class reset_password_form (forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('password1','password2')

    def clean(self):
        cleaned_data = super().clean()
        first_password = cleaned_data.get('password1')
        second_password = cleaned_data.get('password2')
        if first_password and second_password:
            if first_password == second_password:
                return cleaned_data
            else :
                raise forms.ValidationError("passwords are not the same")