from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. This is my blog page.")

def detail(request, post_id):
    return HttpResponse("You're looking at blog post %s." % post_id)

def comment(request, post_id):
    return HttpResponse("You're commenting on post %s." % post_id)