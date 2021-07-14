from django.shortcuts import render
from django.http import HttpResponse
from .models import Sequence
from main_app.forms import Sequence_Form



# Create your views here.

def home(request):
    form = Sequence_Form()
    return render(request, 'home.html', {'form': form})

def result1(request):
    if request.method == 'GET':
            f = open('main_app/static/blast_query_output.txt') 
            file_content = f.read()
            f.close()
            return HttpResponse(file_content, content_type='text/plain')

def result2(request):
    if request.method == 'GET':
            f = open('main_app/static/blast_query_output2.txt') 
            file_content = f.read()
            f.close()
            return HttpResponse(file_content, content_type='text/plain')


