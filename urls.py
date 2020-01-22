from django.urls import path, re_path
from . import views
from django.conf.urls import url
#from django.contrib.auth.views import LoginView



urlpatterns = [
   url(r'^(?P<house_id>[0-9]+)/$', views.detail, name='detail'),
     path('', views.home, name='rentalapp-home'),
    path('about/', views.about, name='rentalapp-about'),
    path('contact/', views.contact, name='rentalapp-contact'), 
    path('information/', views.information,name='information'),
 ]