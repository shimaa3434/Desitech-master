from django.urls import path , include
from accounts.views import CompanyView , JobSeekerView  , LogView , ResetPasswordView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "accounts"

urlpatterns = [
 
    path('company/signup/', CompanyView.signup.as_view(), name='company_signup'),
    
    path('job_seeker/signup/', JobSeekerView.signup.as_view(), name='job_seeker_signup'),

    path('login/', LogView.log_user.as_view(), name='login'),
    
    path('logout/', LogView.logout_user, name='logout'),

    path("password_reset/", ResetPasswordView.ResetPassword.as_view(), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html" 
    , success_url = reverse_lazy ('accounts:password_reset_complete')), name='password_reset_confirm'),
    
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html') , name='password_reset_complete')
    ]

   