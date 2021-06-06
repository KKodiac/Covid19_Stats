from django.shortcuts import render
from .scrape import parse_data
import json
# Create your views here.


def map_korea(request):
    datarray_all, datarray_chart = parse_data()
    context = {
        'array' : json.dumps(datarray_chart),
        'array_all' : json.dumps(datarray_all),
    }
    return render(request, 'map/index_korea.html', context)

def map_world(request):
    context = {
        'test' : "Test"
    }
    return render(request, 'map/index_world.html', context)