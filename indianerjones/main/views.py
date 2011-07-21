from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from haystack import forms
from main.models import *
import datetime
import json

def index(request):
    if request.method == 'GET' and "q" in request.GET:
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            result = form.search().all()    
            return render_to_response('search.html', {'form':form, 'res':result})
        else:
            return render_to_response('search.html', {'form':form,'new':True})
    else:
        form = forms.SearchForm()
        return render_to_response('search.html', { 'form': form, 'new':True })

def display(request, student_id):
    return render_to_response('display.html', {'id': student_id})

def ajax_studentdata(request):
    response = HttpResponse()
    try:
        student_id = request.GET["id"].split(',')
        students = Student.objects.filter(id__in=student_id).select_related()
        #sv = student.values('first_name', 'middle_name', 'last_name', 'publish_date', 'title', 'subtitle', 'isbn')
        result_list = []
        for student in students:
            department = student.department.name
            university = student.department.university.name
            country = student.department.university.country.name
            links = map(lambda l: {'name':l.name, 'url':l.url}, student.link_set.all())
            advisers = map(lambda a: a.pk, student.adviser.all())
            advised = map(lambda a: a.pk, student.student_set.all())
            student_dict = {'first_name': student.first_name, 'middle_name': student.middle_name, 
                    'last_name': student.last_name, 'publish_date': student.publish_date,
                    'title':student.title, 'subtitle': student.subtitle, 'isbn': student.isbn,
                    'country':country, 'university': university, 'department':department, 
                    'links':links, 'advisers':advisers, 'advised':advised}
            result_list.append(student_dict)
        json.dump(result_list, response,  ensure_ascii=False)
    except (KeyError, Student.DoesNotExist): 
        raise Http404
    return response
