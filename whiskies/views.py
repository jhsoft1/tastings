from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models


class NewWhiskyForm(forms.Form):
    name = forms.CharField(label='Whisky name')
    distillery = forms.CharField(label='Distillery')


def index_view(request):
    return render(request, "whiskies/home.html", {'whiskies': models.Whisky.objects.all})


def new_view(request):
    if request.method == 'GET':
        new_whisky_form = NewWhiskyForm()
        return render(request, "whiskies/new.html", {'new_whisky_form': new_whisky_form})
    else:
        if request.user.is_staff:
            name = request.POST.get('name')
            distillery = request.POST.get('distillerie')
            new_whisky = models.Whisky.objects.create(name=name, distillery=distillery, author=request.user)
            return redirect('/')
        else:
            return HttpResponse(status=403)
