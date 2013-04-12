from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
import json
import os
from django.conf import settings
import datetime

data = eval(open(os.path.join(settings.STATIC_ROOT, 'data.txt')).read())
data.sort(key=lambda item:item["time"])
newData = []
for score in data:
	newScore = {"value":score["value"], "time":score['time'].strftime("%d %b %y %H %M %S")}
	print newScore
	newData.append(newScore)
#f = open(os.path.join(settings.STATIC_ROOT, 'data.json'), 'w')
print "new data", newData
#json.dump(newData, f)

def index(request):
	return render(request, 'index.html', {})

def data(request):
	return HttpResponse(json.dumps(newData), mimetype="application/json")