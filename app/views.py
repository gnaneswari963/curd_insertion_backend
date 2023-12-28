from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    tn=input('enter topic name : ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    d={'topic':to}
    return HttpResponse('topic created')

def insert_webpage(request):
    tn=input('enter topic name : ')
    n=input('enter name : ')
    u=input('enter url : ')
    e=input('enter email : ')
    to=Topic.objects.get(topic_name=tn)
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u,email=e)[0]
    wo.save()
    d={'webpage':wo}
    return HttpResponse('webpage created')

def insert_access_record(request):
    pk=int(input('enter pk value of webpage : '))
    n=input('enter name : ')
    d=input('enter date : ')
    a=input('enter author : ')
    wo=Webpage.objects.get(pk=pk)
    aro=AccessRecord.objects.get_or_create(name=wo,date=d,author=a)[0]
    aro.save()
    d={'access_record':aro}
    return HttpResponse('access record created')
