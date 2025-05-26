from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def homepage(request):
  #get the user name parameter. I think this will return None if it's not provided
  user_name = request.GET.get('user_name')
  paramDict = {'user_name' : user_name}

  return render(request, 'base.html', paramDict)