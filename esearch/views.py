from django.shortcuts import render

# Create your views here.
from esearch import es_call
from django.db import connection
from django.http import HttpResponse 

def search_index(request):
        course_term = ""
        city = ""
        term=1
        if request.GET.get('course') and request.GET.get('city'):
            course_term = request.GET['course']
            city = request.GET['city']
            term=2
        elif request.GET.get('course'):
            course_term = request.GET['course']
            term=1
        elif request.GET.get('city'):
            city = request.GET['city']
            term=1
        search_term = course_term or city
        results = es_call.esearch(college_course_name = course_term,city=city,term=term)
        context = {'results': results, 'count': len(results), 'search_term':  search_term}
        
        return render(request,  'index.html',  context)










