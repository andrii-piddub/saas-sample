import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit


def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count()*100)/qs.count()
    except:
        percent = 0
    my_page='home.html'
    my_title = 'New page'
    context={
        'my_title':my_title,
        'page_visits_count':page_qs.count(),
        'percent':percent,
        'total_visits_count':qs.count(),  
            }
    path=request.path
    print('path',path)
    PageVisit.objects.create(path=request.path)
    return render(request, my_page,context)