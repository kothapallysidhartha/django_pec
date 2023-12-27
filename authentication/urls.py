from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('createaccount',views.createaccount, name='createaccount'),
   path('activate/<uidb64>/<token>', views.activate, name='activate'),
   path('cltlogin',views.cltlogin, name='cltlogin'),  
   path('signout',views.signout, name='signout'),
]
