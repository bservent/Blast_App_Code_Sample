from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')

def read_file(request):
    f = open('main_app/static/blast_query_output.txt')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type='text/plain')