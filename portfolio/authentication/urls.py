from django.urls import path
from . import views

urlpatterns=[
path('',views.authlogin, name='login'),
path('forgetpassword/',views.forgetpassword, name='forgetpassword'),
path('register/',views.register, name='register'),
path('logout/',views.authlogout, name='logout'),


]
