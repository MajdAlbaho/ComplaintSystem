from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Profile, Complaint

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_admin:
                return redirect('admin_complaints_view')
            else:
                return redirect('user_complaints_view')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def admin_only(view_func):
    def wrapper_function(request,*args,**kwargs):
        if request.user.profile.is_admin:
            return view_func(request,*args,**kwargs)
        else:
            return redirect('user_complaints_view')
    return wrapper_function

def allow_user(view_func):
    def wrapper_fun(request,*args,**kwargs):
        id_comp=kwargs.get('id')
        user = request.user
        if not user:
            return redirect('login')
        log_in_user = User.objects.filter(username=request.user.username).first()
        complaints = Complaint.objects.filter(id=id_comp).first()

        if log_in_user.id==complaints.author.id or log_in_user.profile.is_admin:

            return view_func(request,*args,**kwargs)
        else:
            return HttpResponse("Access denied")
    return wrapper_fun
