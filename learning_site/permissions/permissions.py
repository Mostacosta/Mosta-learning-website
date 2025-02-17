from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect

user_login_required = user_passes_test(lambda user: user.is_active, login_url= "/login" )

def active_user_required(view_func):
    decorated_view_func = login_required(user_login_required(view_func))
    return decorated_view_func