from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def htmlforms(request):

    if request.method=='POST':
        return HttpResponse(request.POST['username'])
    return render(request,'htmlforms.html')


def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Topic is created')



    return render(request,'insert_topic.html')


def insert_webpage(request):

    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        tn=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']

        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('Webpage is created')




    return render(request,'insert_webpage.html',d)

def select_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        topics=request.POST.getlist('topics')
        print(topics)
        webpages=Webpage.objects.none()
        for tn in topics:
            webpages=webpages|Webpage.objects.filter(topic_name=tn)
        d1={'webpages':webpages}
        return render(request,'display_webpages.html',d1)
    return render(request,'select_topic.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}


    return render(request,'checkbox.html',d)


def update_webpage(request):
    #Webpage.objects.filter(name='ro').update(email='Ro@gmail.com')
    #Webpage.objects.filter(topic_name='Cricket').update(email='India@gmail.com')
    #Webpage.objects.filter(name='ko').update(topic_name='Cricket')
    #Webpage.objects.filter(name='eo').update(topic_name='Rugby')
    #Webpage.objects.filter(name='eod').update(topic_name='Cricket')
    #Webpage.objects.update_or_create(name='ko',defaults={'url':'https://ko.in'})
    #Webpage.objects.update_or_create(topic_name='Cricket',defaults={'url':'https://India.com'})
    CTO=Topic.objects.get(topic_name='Foot Ball')
    #Webpage.objects.update_or_create(name='rohit',defaults={'topic_name':CTO})
    Webpage.objects.update_or_create(name='Harshad',defaults={'url':'https://India.com','topic_name':CTO})









    webpages=Webpage.objects.all()
    d1={'webpages':webpages}
    return render(request,'display_webpages.html',d1)


def delete_webpage(request):
    #Webpage.objects.filter(name='ko').delete()
    Webpage.objects.all().delete()
    webpages=Webpage.objects.all()
    d1={'webpages':webpages}
    return render(request,'display_webpages.html',d1)






