from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("成功！！！！！！！")


def login(request):
    return render(request,'register.html')