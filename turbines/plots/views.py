import base64
import io
import urllib
from typing import Dict, Union, Any

from django.shortcuts import render
from . import old_load_from_mongo as load_mongo
from .forms import InputForm


def home(request):
    submit_button = request.POST.get("submit")
    end = ""
    start = ""
    form = InputForm(request.POST)
    context = {'form': form, 'end': end, 'start': start, 'submit_button': submit_button}
    if form.is_valid():
        end = form.cleaned_data.get("end")
        start = form.cleaned_data.get("start")
        fig, start , end = load_mongo.get_my_fig(start, end)
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        context = {'end': end, 'start': start, 'data': uri}
        return render(request, 'plot.html', context)
    return render(request, 'home.html', context)

""" if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        start = request.POST.get('start')
        end = request.POST.get('end')
        fig = load_mongo.get_my_fig(start, end)
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        return render(request, 'plot.html', {'data': uri, 'start': start, 'end': end})
    return render(request, 'home.html')"""

