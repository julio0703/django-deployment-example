from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'ApplicationTwo/index.html')

def second(request):
    return render(request,'ApplicationTwo/second.html',
                         {'template_tag':'THIS IS A TEMPLATE TAG... WITH A FILTER.'})

def third(request):
    return HttpResponse('This is an example of a HttpResponse without html.')

def fourth(request):
    return HttpResponse('<p><strong>This is HttpResponse with html.</strong></p>')
