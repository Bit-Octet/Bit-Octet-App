from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# cd Users\josch\BO_web_app\BO_app
# python manage.py runserver

# Create your views here.
def index(request):
    return render(request, 'polls/index.html')
    #return HttpResponse(b"Hello, world. You're at the polls index.")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})