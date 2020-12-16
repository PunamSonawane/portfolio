from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pfapp(request):
    return HttpResponse("This is the Portfolio app page")
def profile(request):
    return render(request,'pftemplates/profile.html')
