from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *

# Create your views here.
def insert_Topic(request):
    tn=input('enter tn')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('data is inserted')

def insert_Webpage(request):
    tn=input('enter tn')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    name=input('enter n')
    url=input('enter u')
    WO=Webpage.objects.get_or_create(topic_name=tn,name='n',url='u')[0]
    return HttpResponse('data is inserted')


def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)
    
def display_webpages(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    webpages=Webpage.objects.filter(topic_name='vollyball')
    return render(request,'dispaly_webpages.html',d)
