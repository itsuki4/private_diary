from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.


def index(request):
    msg = request.GET['msg']
    return render(request, 'index.html')
