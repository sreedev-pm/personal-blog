from django.shortcuts import render
from .models import blogmodel
def index(request):
    blog=blogmodel.get.object.all()
    return (render(request,'index.html',{'blogs':blog}))
