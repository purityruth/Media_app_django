from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import MediaForm
from django.contrib import messages
# Create your views here.

def home(request):
    media = Media.objects.all()
    customers = User.objects.all()
    context = { 'customers' : customers, 'media' : media }
    return render(request, 'accounts/dashboard.html', context)

def user(request):
    media_user = User.objects.all()
    context = { 'media_user' : media_user }
    return render(request, 'accounts/dashboard.html', context)

def createMedia(request):

    form = MediaForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = { 'form' : form}
    return render(request, 'accounts/media_form.html', context)

def updateMedia(request, pk):
    media = Media.objects.get(id=pk)
    form = MediaForm(instance=media)
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = MediaForm(request.POST, instance=media)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = { 'form' : form}
    return render(request, 'accounts/media_form.html', context)

def deleteMedia(request, pk):

    media = Media.objects.get(id=pk)
    if request.method == "POST":
        media.delete()
        messages.success(request,'Successfully deleted!')
        return redirect('/')
    context = { 'item' : media}
    return render(request, 'accounts/delete.html', context)
