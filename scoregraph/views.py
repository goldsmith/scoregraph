from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
import json
import os
from django.conf import settings
import datetime

data = eval(open(os.path.join(settings.STATIC_ROOT, 'data.txt')).read())
data.sort(key=lambda item:item["time"])
newData = []

print "here"

currentDay = data[0]['time']
total = 0
count = 0

print "and here"

for score in data:

	print "score!"
	print "score['time'].day", score['time'].day
	print "currentDay", currentDay

	if score['time'].day == currentDay.day:

		print 'scorevalue', score['value']

		total += score['value']
		count += 1

		print "all good"
	else:

		newScore = {"value":float(total)/count, "time":currentDay.strftime("%d %b %y %H %M %S")}
		newData.append(newScore)
		currentDay = score['time']
		total = score["value"]
		count = 1

		print "awesomely"

print "new data", newData

def index(request):
	return render(request, 'index.html', {})

def data(request):
	return HttpResponse(json.dumps(newData), mimetype="application/json")