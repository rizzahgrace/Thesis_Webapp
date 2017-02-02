from django.http import HttpResponse
from django.shortcuts import render
from .models import RawData
from webapp.forms import UploadCSVFile
from webapp.utils import handle_upload_file, ChartData
from django.contrib import messages
from chartit import DataPool, Chart

from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from webapp.serializers import DataSerializer

from highcharts.views import (HighChartsMultiAxesView, HighChartsPieView, HighChartsSpeedometerView, HighChartsHeatMapView, HighChartsPolarView)
# Create your views here.
def index(request):
	return render(request, 'webapp/highchart_script.html')

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
def weather_chart_view(request):
	#Step 1: Create a DataPool with the data we want to retrieve.
	weatherdata = DataPool(
		series=
			[{'options': {
				'source': RawData.objects.all()},
				'terms': [
				'winddir',
				'rainin']}
			])
	cht = Chart(
			datasource = weatherdata,
			series_options =
				[{'options':{
					'type': 'line',
					'stacking': False},
				'terms':{
					'winddir': [
					'rainin']
				}}],
			chart_options =
				{'title': {
					'text': 'Weather Data of Boston and Houston'},
					'xAxis': {
					'title': {
					'text': 'Rain in'}}})
	return render_to_response('webapp/home.html', {'weatherchart': cht})

class DataListView(APIView):
	def get(self, request):
		data = RawData.objects.values('winddir', 'rainin')
		return Response(data)

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def rawdatalist(request):
	if request.method == 'GET':
		rawdata = RawData.objects.all()
		serializer = DataSerializer(rawdata, many=True)
		return JSONResponse(serializer.data)


def plot(request, chartID = 'rawdatachart', chart_type = 'line', chart_height = 500):
	data = ChartData.raw_data()
	title = "{text:'Raw Data'}"
	xAxis = {"title": {"text": 'Timestamp'}, "categories": data['timestamp']}
	yAxis = {"title": {"text": 'Data'}}
	series = [
		{"name": 'Temperature (F)', "data": data['tempf']}, 
		{"name": 'Wind Speed', "data": data['windspeedmph']},
		{"name": 'Rain', "data": data['rainin']}
		]
	return render(request, 'webapp/highchart_script.html', {'chartID': chartID, 'title': title,'xAxis': xAxis, 'yAxis': yAxis, 'series':series})

class BarView(HighChartsMultiAxesView):
	title = 'Example Data Chart'
	subtitle = ''
	categories = ['Orange', 'Bananas', 'Apples']
	chart_type = ''
	chart = {'zoomType': 'xy'}
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
	title = 'Advanced graph'
	subtitle = 'params and query'
	chart = {'zoomType': 'xy'}
	tooltip = {'shared': 'true'}
	legend = {
		'layout': 'vertical',
		'align': 'left',
		'verticalAlign': 'top',
		'y': 30
	}

	def get_data(self):
		f = RawData.objects.all()
		cursor = connection.cursor()
		# cursor.execute("SELECT timestamp, winddir from rawdata", [f.pk])
		graph = cursor.fetchall()
		timestamp = list()
		winddir = list()

		for i in range(0, len(graph)):
			timestamp.append(rows[i][9])
			winddir.append(rows[i][3])

		#### SERIES
		self.serie = graph[0]

		##### X LABELS
		self.categories = graph[1]

		##### Y AXIS DEFINITIONS
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

		##### SERIES WITH VALUES
		self.series = self.serie
		data = super(AdvancedGraph, self).get_data()
		return data