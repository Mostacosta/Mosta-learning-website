from .forms import user_form,profile_form,reset_password_form,reset_password_mail,change_password_form
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from .models import teacher
from django.contrib import messages

# Create your views here.
def create_user (request):
    userform = user_form()
    profileform = profile_form()

    if request.method == 'POST':
        userform = user_form(request.POST)
        profileform = profile_form(request.POST, request.FILES)

        if userform.is_valid() and profileform.is_valid() :
            user = userform.save()
            user.set_password(user.password)
            user.is_active=False
            user.save()
            profile = profileform.save(commit=False)
            profile.user = user
            profile.save()
            current_site = get_current_site(request)
            print(user.pk)
            print(urlsafe_base64_encode(force_bytes(user.pk)))
            mail_subject = 'Activate your blog account.'
            message = render_to_string('contacts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = userform.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse("check your mail")
        else:
            messages.error(request,userform.errors.as_text()+profileform.errors.as_text())

    return render(request,'contacts/sign-up.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def forgot_password_mail(request):
    form = reset_password_mail()
    if request.method == "POST":
        form = reset_password_mail(request.POST)
        if form.is_valid :
            mail = request.POST['email']
            user = User.objects.filter(email=mail)
            if user is not None :
                user = user[0]
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account.'
                message = render_to_string('contacts/acc_reset_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                email = EmailMessage(
                    mail_subject, message, to=[mail]
                )
                email.send()
                return HttpResponse('Check your mail ')

    return render(request,'contacts/resetmail.html',{'form':form})

def reset_password(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        form = reset_password_form()
        if request.method == "POST":
            form =reset_password_form(request.POST)
            if form.is_valid() :
                user.password = request.POST['password1']
                user.set_password(user.password)
                print(user.password)
                user.save()
                return HttpResponse('you have a new password nw .')
        return render(request,'contacts/resetpassword.html',{'form':form})

    else:
        return HttpResponse('Activation link is invalid!')

        
@login_required
def change_password (request):
    form = change_password_form()

    if request.method == 'POST':
        form = change_password_form(request.POST)
        if form.is_valid():
            user = request.user
            print(user.username)
            old_password = request.POST['old_password']

            if check_password(old_password,user.password):
                user.password = request.POST['password1']
                user.set_password(user.password)
                user.save()
                return HttpResponse('you have a new password nw .')
            else:
                return HttpResponse('the password is wrong .')


    return render(request,'contacts/resetpassword.html',{'form':form})

def teacher_details (request,pk):
    teacher_ = teacher.objects.get(pk=pk)
    return render (request,'contacts/teacher.html',{"teacher":teacher_})
