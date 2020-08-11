
from django.shortcuts import render , HttpResponse , redirect
from django.views import View
from django.contrib.auth import login , logout 
from accounts.forms import UserForm , JobSeekerForm
from accounts.models.User import User


# Create your views here.

class signup (View):

    def get(self, request):
        
        user_form = UserForm.signup_form ()
        JobSeeker_profile_form = JobSeekerForm.signup_form ()

        context = {'user_form' : user_form , 'JobSeeker_profile_form' : JobSeeker_profile_form ,  'page_title' : 'job seeker signup' }
        return render (request , 'jobseeker_signup.html' , context)

    def post (self, request):

        user_form = UserForm.signup_form(request.POST)
        JobSeeker_profile_form = JobSeekerForm.signup_form (request.POST)
        
        if user_form.is_valid() and JobSeeker_profile_form.is_valid():
            user = user_form.save(commit=False)
            job_seeker_profile = JobSeeker_profile_form.save(commit=False)

            user.user_type = User.JOB_SEEKER
            job_seeker_profile.user = user

            user_form.save()
            JobSeeker_profile_form.save()
           
            login(request , user)
            return redirect ('/' )
        else:
            context = {'user_form' : user_form , 'JobSeeker_profile_form' : JobSeeker_profile_form , 'page_title' : 'job seeker signup' }
            return render (request , 'jobseeker_signup.html' , context)
      
