
from django.shortcuts import render , HttpResponse , redirect
from django.views import View
from django.contrib.auth import login , logout 
from accounts.forms import UserForm , CompanyForm
from accounts.models.User import User


# Create your views here.

class signup (View):

    def get(self, request):
        
        user_form = UserForm.signup_form ()
        company_profile_form = CompanyForm.signup_form ()

        context = {'user_form' : user_form , 'company_profile_form' : company_profile_form , 'page_title' : 'company signup' }
        return render (request , 'company_signup.html' , context)

    def post (self, request):

        user_form = UserForm.signup_form(request.POST)
        company_profile_form = CompanyForm.signup_form (request.POST)
        
        if user_form.is_valid() and company_profile_form.is_valid():
            user = user_form.save(commit=False)
            company_profile = company_profile_form.save(commit=False)

            user.user_type = User.COMPANY
            company_profile.user = user

            user_form.save()
            company_profile.save()
           
            login(request , user)
            return redirect ('/' )
        else:
            context = {'user_form' : user_form , 'company_profile_form' : company_profile_form , 'page_title' : 'company signup' }
            return render (request , 'company_signup.html' , context)
      
