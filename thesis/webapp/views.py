import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import RawData_Weather, RawData_AMPS
from webapp.forms import UploadCSVFile
from webapp.utils import handle_upload_file
from webapp.forms import recordOwner
from django.contrib import messages
from chartit import DataPool, Chart

from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from webapp.serializers import DataSerializer

from highcharts.views import (HighChartsMultiAxesView, HighChartsPieView, HighChartsSpeedometerView, HighChartsHeatMapView, HighChartsPolarView, HighChartsStockView)
# Create your views here.
def loading(request):
	return render(request, 'webapp/loading.html')

def login(request):
	return render(request, 'webapp/login.html')

def index(request):
	return render(request, 'webapp/index.html')

def weather(request):
	return render(request, 'webapp/weather.html')

def csv(request):
	if request.method == 'POST':
		form = UploadCSVFile(request.POST, request.FILES)
		
		if form.is_valid():
			owner = form.cleaned_data['owner']
			handle_upload_file(request.FILES['csvfile'], owner)
			messages.success(request, 'Record saved')
	else:
		form = UploadCSVFile()

	return render(request, 'webapp/csv.html', {'form': form})

#for using Chartit
#error says Nonetype object not subscriptable
def register(request):
	if request.method == 'POST':
		form = recordOwner(request.POST)
		if form.is_valid():
			last_name = form.cleaned_data['last_name']
			first_name = form.cleaned_data['first_name']
			address = form.cleaned_data['address']
			record = Owner(last_name=last_name, first_name=first_name, address=address)
			record.save()
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			email=form.cleaned_data['email']
			)
			messages.success(request, 'Record saved')            
	else:
		form = recordOwner()
	return render(request, 'webapp/login.html', {'form': form})

class AdvancedGraph(HighChartsMultiAxesView):
	title = 'Example Data Chart'
	subtitle = ''
	chart_type = ''
	chart = {'zoomType': 'xy'}
	tooltip = {'shared': 'true'}
	legend = {
		'layout': 'vertical',
		'align': 'left',
		'verticalAlign': 'top',
		'y': 30
	}

	def get_data(self):
		data = {'id': [], 'winddir': [], 'rainin':[], 'timestamp':[]}
		f = RawData_Weather.objects.all()
		for unit in f:
			data['id'].append(unit.id)
			data['timestamp'].append(unit.timestamp.strftime('%I:%M'))
			data['winddir'].append(unit.winddir)
			data['rainin'].append(unit.rainin)


		self.categories = data['timestamp']
		
		self.yaxis = {
			'title': {
				'text': 'Title 1'
			},
			'plotLines': [
				{
					'value': 0,
					'width': 1,
					'color': '#808080'
				}
			]
		}
		self.serie = [
			{
			'name': 'Winddir',
			'data': data['winddir']
			}
			# {
			# 'name': 'Rainin',
			# 'data': data['rainin']
			# } 
		]

		##### X LABELS
		# self.axis = data['id']
		

		##### SERIES WITH VALUES
		self.series = self.serie
		data = super(AdvancedGraph, self).get_data()
		return data

# int(time.mktime(unit.timestamp.timetuple())*1000)

class PowerGraph(HighChartsMultiAxesView):
	title = 'Power'
	subtitle = ''
	chart_type = ''
	chart = {'zoomType': 'xy'}
	tooltip = {'shared': 'true'}
	legend = {
		'layout': 'vertical',
		'align': 'left',
		'verticalAlign': 'top',
		'y': 30
	}

	def get_data(self):
		data = {'id': [], 'load': [], 'SP_volt':[], 'timestamp':[]}
		f = RawData_AMPS.objects.all()
		for unit in f:
			data['id'].append(unit.id)
			data['timestamp'].append(datetime.datetime.strptime(unit.timestamp, '%m/%d/%Y %H:%M'))
			data['load'].append(unit.load)
			data['SP_volt'].append(unit.SP_volt)


		self.categories = data['timestamp']
		
		self.yaxis = {
			'title': {
				'text': 'Title 1'
			},
			'plotLines': [
				{
					'value': 0,
					'width': 1,
					'color': '#808080'
				}
			]
		}
		self.serie = [
			{
			'name': 'Load',
			'data': data['load']
			},
			{
			'name': 'Voltage',
			'data': data['SP_volt']
			} 
		]

		##### X LABELS
		# self.axis = data['id']
		

		##### SERIES WITH VALUES
		self.series = self.serie
		data = super(PowerGraph, self).get_data()
		return data