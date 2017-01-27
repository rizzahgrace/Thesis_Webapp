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

# Create your views here.
def index(request):
	return render(request, 'webapp/home.html')

def csv(request):
	if request.method == 'POST':
		form = UploadCSVFile(request.POST, request.FILES)
		
		if form.is_valid():
			handle_upload_file(request.FILES['csvfile'])
			messages.success(request, 'Record saved')
	else:
		form = UploadCSVFile()

	return render(request, 'webapp/csv.html', {'form': form})

def weather_chart_view(request):
	#Step 1: Create a DataPool with the data we want to retrieve.
	weatherdata = DataPool(
		series=
			[{'options': {
				'source': RawData.objects.all()},
				'terms': [
				'timestamp',
				'winddir']}
			])
	cht = Chart(
			datasource = weatherdata,
			series_options =
				[{'options':{
					'type': 'line',
					'stacking': False},
				'terms':{
					'timestamp': [
					'winddir']
				}}],
			chart_options =
				{'title': {
					'text': 'Weather Data of Boston and Houston'},
					'xAxis': {
					'title': {
					'text': 'Rain in'}}})
	return render_to_response(home.html, {'weatherchart': cht})

class DataListView(APIView):
	def get(self, request):
		data = RawData.objects.values('winddir')
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