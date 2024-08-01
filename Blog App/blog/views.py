from django.shortcuts import render,redirect
from .models import webdata
from django.http import HttpResponse
from django import forms
from .forms import webform

# Create your views here.
def post_list(request):
    data=webdata.objects.all()
    all_data={
        'data':data
    }
    print(data)
    return render(request,'list.html',all_data)


def add_blog(request):
    form=webform()
    if request.method=='POST':
        form=webform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('List')
    context={
            'form':form
    }
    return render(request,'input.html',context)

def single_blog(request,id):
    single=webdata.objects.get(id=id)
    singleblog={
        'single':single
    }
    return render(request,'single_blog.html',singleblog)