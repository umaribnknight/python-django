from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return remder (request)
    print(request.user)
    return HttpResponse("<h1>Welcome user"</h1>".format(user))