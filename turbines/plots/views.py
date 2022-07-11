import base64
import io
import urllib
from django.shortcuts import render
from . import old_load_from_mongo as load_mongo


def home(request):
    start = "20000101 00:00"
    end = "20500101 00:00"
    #if request.method == 'POST':
    #    start = request.POST.get('start', None)
    #    end = request.POST.get('end', None)
    fig = load_mongo.get_my_fig(start, end)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'home.html', {'data': uri})

