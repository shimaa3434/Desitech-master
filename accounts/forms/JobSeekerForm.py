from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from accounts.models.JobSeekerProfile import job_seeker_profile
from accounts.models.City import City

class signup_form (forms.ModelForm):

    class Meta:
        model = job_seeker_profile
        fields = ('Name' , 'surname' , 'country' , 'city' , 'country_of_residence','age'
                    ,'gender' , 'street' , 'zip_code' ,
                     'house_number' , 'personal_photo'  , 'CV' ,
                     'cover_letter' , 'phone_number' , 'mobile_number' ,)
        labels = {
            'Name': '', 'surname': '', 'country': '', 'city': '', 'country_of_residence': '',
            'age' : '', 'gender':'', 'zip_code': '', 'street': '', 'house_number': '', 'personal_photo': 'Personal_Photo',
            'CV': 'Upload CV File', 'cover_letter': '', 'phone_number': '','mobile_number': '',
        }
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name "}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Surname"}),
            'country': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': "Country ", 'id': 'country'}),
            'city': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': "city ", 'id': 'city'}),
            'country_of_residence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Country Of Residence"}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Age"}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Gender"}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Zip Code"}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Street "}),
            'house_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "House Number"}),
            'personal_photo': forms.FileInput(attrs={'class': 'custom-file-input', 'placeholder':"Personal_Photo" , 'id': 'photo'}),
            'CV': forms.FileInput(attrs={'class': 'custom-file-input', 'placeholder': "Upload Your CV File", 'id': 'CVFile'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Cover Letter", 'rows':"6", 'id': 'coverletter'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "phone Number", 'type': 'tel'}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "mobile Number", 'type': 'tel'}),
        }
                    
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['city'].queryset = City.objects.none()
        
            if 'country' in self.data:
                try:
                    country_id = int(self.data.get('country'))
                    self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
                except (ValueError, TypeError):
                    pass 
            elif self.instance.pk:
                self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
