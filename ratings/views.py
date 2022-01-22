from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models


class NewRatingForm(forms.Form):
    whisky = forms.CharField(label='Whisky')
    nose = forms.CharField(label='Nose')
    taste = forms.CharField(label='Taste')
    color = forms.CharField(label='Color')
    smokiness = forms.CharField(label='Smokiness')


def new_view(request):
    if request.method == 'GET':
        new_rating_form = NewRatingForm()
        return render(request, "ratings/new.html", {'new_rating_form': new_rating_form})
    else:
        if request.user.is_authenticated:
            whisky = request.POST.get('whisky')
            nose = request.POST.get('nose')
            taste = request.POST.get('taste')
            color = request.POST.get('color')
            smokiness = request.POST.get('smokiness')
            new_rating = models.Rating.objects.create(whisky=whisky, nose=nose, taste=taste, color=color,
                                                      smokiness=smokiness,author=request.user)
            return redirect('/')
        else:
            return HttpResponse(status=403)


def index_view(request):
    return render(request, "ratings/home.html", {'ratings': models.Rating.objects.all})
