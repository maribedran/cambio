# coding: utf-8
from django.shortcuts import render
import requests

response = requests.get('http://jsonrates.com/historical/?'+
	'from=USD'+
	'&to=BRL'+
    '&dateStart=2014-11-14'+
    '&dateEnd=2014-11-20'
)

json = response.json()

week_rates = {}

for date, values in json['rates'].iteritems():
    histrate = float(values['rate'])
    week_rates[date] = histrate

def index(request):
 return render(request, 'home/index.html', week_rates)