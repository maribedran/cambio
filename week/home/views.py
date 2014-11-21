# coding: utf-8
from django.shortcuts import render
import requests
from datetime import date, timedelta
import collections

today = date.today()
last_week = today - timedelta(7)

def get_currency(currency):
	response = requests.get('http://jsonrates.com/historical/?'+
		'from='+
		currency+
		'&to=BRL'+
	    '&dateStart='+ str(last_week)+
	    '&dateEnd='+ str(today)
	)

	json = response.json()

	week_rates = {}

	for date, values in json['rates'].iteritems():
	    histrate = round(float(values['rate']), 2)
	    utc_date = values['utctime']
	    week_rates[utc_date] = histrate

	week_rates = collections.OrderedDict(sorted(week_rates.items()))

	return week_rates

def get_name(currency):
	if currency == 'USD':
		currency_name = 'Dólar'
	elif currency == 'EUR':
		currency_name = 'Euro'
	elif currency == 'ARS':
		currency_name = 'Pesos argentinos'

	return currency_name

def dolar(request):
	week_rates = get_currency('USD')
	currency_name = get_name('USD')
	return render(request, 'home/index.html', {'week_rates' : week_rates, 'currency_name' : currency_name})

def euro(request):
	week_rates = get_currency('EUR')
	currency_name = get_name('EUR')
	return render(request, 'home/euro.html', {'week_rates' : week_rates, 'currency_name' : currency_name})

def peso(request):
	week_rates = get_currency('ARS')
	currency_name = get_name('ARS')
	return render(request, 'home/peso.html', {'week_rates' : week_rates, 'currency_name' : currency_name})