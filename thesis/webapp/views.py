from django.http import HttpResponse
from django.shortcuts import render
from .models import RawData
from webapp.forms import UploadCSVFile
from webapp.utils import handle_upload_file, ChartData
from django.contrib import messages

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

# class JSONResponse(HttpResponse):
# 	"""
# 	An HttpResponse that renders its content into JSON.
# 	"""
# 	def __init__(self, data, **kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type'] = 'application/json'
# 		super(JSONResponse, self).__init__(content, **kwargs)

class DataListView(APIView):
    def get(self, request):
        data = RawData.objects.values('winddir')
        return Response(data)

@csrf_exempt
def rawdatalist(request):
	"""
	List all code snippets, or create a new snippet.
	"""
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