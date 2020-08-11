from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render , redirect ,HttpResponse
from django.views import View
from accounts.models.User import User
from accounts.models.CompanyProfile import Company_profile
from accounts.models.JobSeekerProfile import job_seeker_profile
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from Desitech.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string

class ResetPassword (View):
    
    def get (self , request) :
        password_reset_form = PasswordResetForm()
        context={"password_reset_form":password_reset_form , 'page_title' : 'Reset Password'}
        return render(request,"password/password_reset.html", context)

    def post (self , request) :
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                  
                    if user.is_superuser :
                        name = 'Admin'
                    else:
                        name = user.getProfile().Name
                   
                    subject = "Password Reset Requested"
                    email_template_name = "password/reset_Email.txt"
                  
                    info = {
					"user": user,
					'full_user_name' : name, 
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Desitech',
					'uid': urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http'}

                    email = render_to_string(email_template_name, info)
                    
                    try:
                        send_mail(subject, email, EMAIL_HOST_USER , [user.email], fail_silently=False)
                    except Exception:
                        return HttpResponse('Invalid request, check your internet connection or try again !!.')

                    return redirect ("/accounts/password_reset/done/")   
