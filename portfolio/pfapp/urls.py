from django.urls import path
from . import views

urlpatterns=[
path('new/',views.pfapp),
path('profile/',views.profile, name='profile'),

]
