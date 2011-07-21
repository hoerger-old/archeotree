from django.http import HttpResponse
from django.shortcuts import render_to_response
from haystack import forms
import datetime

def index(request):
    if request.method == 'GET':
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            result = form.search().all()    
            return render_to_response('search.html', { 'form': form, 'res':result})
    else:
        form = forms.SearchForm()
    return render_to_response('search.html', { 'form': form, })
