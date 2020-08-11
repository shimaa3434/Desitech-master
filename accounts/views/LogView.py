from django.contrib.auth import login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponse , render , redirect
from django.contrib.auth.decorators import login_required
from django.views import View

class log_user(View):

    def get (self,request):
            signin_form = AuthenticationForm ()
            context = {'signin_form' : signin_form , 'page_title' : 'login'}
            return  render (request , 'login.html' , context )


    def post (self ,request) :
            signin_form = AuthenticationForm(data = request.POST)
            if signin_form.is_valid():
                #login user
                user = signin_form.get_user()
                login(request , user)
                return redirect ('/' )
            else:
                context = {'signin_form' : signin_form , 'page_title' : 'login'}
                return  render (request , 'login.html' , context )


@login_required (login_url = 'accounts:login')
def logout_user (request) :
        logout (request)
        return redirect ('/' )
