import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import RawData_Weather, RawData_AMPS
from webapp.forms import UploadCSVFile
from webapp.utils import handle_upload_file
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
			handle_upload_file(request.FILES['csvfile'])
			messages.success(request, 'Record saved')
	else:
		form = UploadCSVFile()

	return render(request, 'webapp/csv.html', {'form': form})

#for using Chartit
#error says Nonetype object not subscriptable

class DataListView(APIView):
	def get(self, request):
		data = RawData_Weather.objects.values('winddir', 'rainin')
		return Response(data)

class BarView(HighChartsMultiAxesView):
	title = 'Example Data Chart'
	subtitle = ''
	categories = ['Orange', 'Bananas', 'Apples']
	chart_type = ''
	chart = {'zoomType': 'x'}
	tooltip = {'shared': 'true'}
	legend = {'layout': 'horizontal', 'align': 'left',
			  'floating': 'true', 'verticalAlign': 'top',
			  'y': -10, 'borderColor': '#e3e3e3'}

	@property
	def yaxis(self):
		y_axis = [
			{'labels': {'format': '{value} pz/sc ', 'style': {'color': '#f67d0a'}},
			 'title': {'text': "Oranges", 'style': {'color': '#f67d0a'}},
			 'opposite': 'true'},
			{'gridLineWidth': 1,
			 'title': {'text': "Bananas", 'style': {'color': '#3771c8'}},
			 'labels': {'style': {'color': '#3771c8'}, 'format': '{value} euro'}},
			{'gridLineWidth': 1,
			 'title': {'text': "Apples", 'style': {'color': '#666666'}},
			 'labels': {'format': '{value} pz', 'style': {'color': '#666666'}},
			 'opposite': 'true'}
		]
		return y_axis

	@property
	def series(self):
		series = [
			{
				'name': 'Orange',
				'type': 'column',
				'yAxis': 1,
				'data': [90,44,55,67,4,5,6,3,2,45,2,3,2,45,5],
				'tooltip': "{ valueSuffix: ' euro' }",
				'color': '#3771c8'
			},
			{
				'name': 'Bananas',
				'type': 'spline',
				'yAxis': 2,
				'data': [12,34,34,34, 5,34,3,45,2,3,2,4,4,1,23],
				'marker': { 'enabled': 'true' },
				'dashStyle': 'shortdot',
				'color': '#666666',
				},
			{
				'name': 'Apples',
				'type': 'spline',
				'data': [12,23,23,23,21,4,4,76,3,66,6,4,5,2,3],
				'color': '#f67d0a'
			}
		]
		return series

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