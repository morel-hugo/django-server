from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from . import charts

#def index(request):
    #info_account = {"balance":1, "fd":2, "marge":3,"nt":4}
    #return render(request,'pages/index.html', {'info_account': info_account,'chart' : charts.info_gauge})

def index(request):
    info_account = {"balance":1, "fd":2, "marge":3,"nt":4}
    return render(request,'pages/index.html', {'info_account': info_account,'chart' : charts.basic_line(),'chart2' : charts.solid_gauge()})
