from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from accounts.models.User import User



class signup_form (UserCreationForm) :
    class Meta:
        model = User
        fields = ('email', 'password1' , 'password2')
        widgets= {
            'email': forms.EmailInput(attrs= {'class': 'form-control', 'placeholder':"Enter your email "}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password confirmation "})
        }
        labels = {'email': '', 'password1': '', 'password2': '',}
        help_texts = { 'email': None, 'password1': None, 'password2': None,
        }





