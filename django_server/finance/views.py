from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from . import charts

#def index(request):
    #info_account = {"balance":1, "fd":2, "marge":3,"nt":4}
    #return render(request,'pages/index.html', {'info_account': info_account,'chart' : charts.info_gauge})

info_account = {"balance":1, "fd":2, "marge":3,"nt":4}



list_index = {'info_account': info_account,'chart' : charts.basic_line(),'gauge_0' : charts.func_solid_gauge()[0],\
'gauge_1' : charts.func_solid_gauge()[1],'gauge_2' : charts.func_solid_gauge()[2],'gauge_3' : charts.func_solid_gauge()[3],\
'chart3' : charts.solid_pie()}

def index(request):
    return render(request,'pages/index.html', list_index)
