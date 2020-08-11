from django.contrib import admin
from django.urls import path , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('accounts/' , include ('accounts.urls') ) ,
    path ('jobs/' , include ('jobs.urls') ) ,
    path ('' , views.index , name='home') ,
    path ('aboutus/' , views.about , name='about-us'),
    path ('contactus/' , views.contact , name='contact-us')
]


if settings.DEBUG:
        urlpatterns+= staticfiles_urlpatterns()
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)