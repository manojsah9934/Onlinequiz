from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.core.paginator import Paginator

lst =[]
answers = Question.objects.all()
anslist = []

for i in answers:

    anslist.append(i.answer)
def welcome(request):
    lst.clear()
    return render(request,'welcome.html')

def quiz(request):
    obj = Question.objects.all()
    paginator = Paginator(obj,1)
    try:
        page = int(request.GET.get('page','1'))
    except:

        page =1
    try:

        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):

        questions=paginator.page(paginator.num_pages)

    return render(request,'quiz.html',{'obj':obj,'questions':questions})

def result(request):
    score =0
    for i in range(len(lst)):

        if lst[i]==anslist[i]:
            score +=1
    return render(request,'result.html',{'score':score,'lst':lst})

def saveans(request):
    ans = request.GET['ans']
    lst.append(ans)
    