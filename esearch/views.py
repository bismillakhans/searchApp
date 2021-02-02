from django.shortcuts import render

# Create your views here.
from esearch import es_call

from django.http import HttpResponse 

def search_index(request):
    results = []
    name_term = ""
    if request.GET.get('name') :
        name_term = request.GET['name']
    results = es_call.esearch(college_course_name = name_term)
    print(results)
    # import pdb; pdb.set_trace()
    context = {'results': results, 'count': len(results), 'search_term':  name_term}
    return render(request,  'index.html',  context)