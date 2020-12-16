from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    text={
    'name':'Punam Sonawane',
    'age':32,
    'phone':647337088,
    'friend_name':['soni','toni','moni']
    }
    return render(request,'index.html',text)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
