import base64
import io
import urllib
import matplotlib.pyplot as plt
from django.shortcuts import render
from load_from_mongo import MongoPlots


def home(request):
    start = False
    end = False
    if request.method == 'POST':
        start_time = request.POST.get('start_time', None)
        end_time = request.POST.get('end_time', None)
        start_date = request.POST.get('start_date', None)
        end_date = request.POST.get('end_date', None)
        #try:

        #except:

    fig = .get_my_fig(start, end)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    if not start:
        start = load_from_mongo.start_date()
    if not end:
        end = load_from_mongo.end_date()

    return render(request, 'home.html', {'data': uri}, {'start': start}, {'end': end})

