import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import RawData_Weather, RawData_AMPS, Owner
from django.contrib.auth.models import User
from webapp.forms import UploadCSVFile, recordOwner, recordUser
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
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
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

@csrf_protect
def register(request):
	if request.method == 'POST':
		userdata_form = recordOwner(request.POST)
		user_form = recordUser(request.POST)
		if userdata_form.is_valid() and user_form.is_valid():
			last_name = userdata_form.cleaned_data['last_name']
			first_name = userdata_form.cleaned_data['first_name']
			address = userdata_form.cleaned_data['address']
			owner = Owner(last_name=last_name, first_name=first_name, address=address)
			user = User.objects.create_user(
			username=user_form.cleaned_data['username'],
			password=user_form.cleaned_data['password1'],
			email=user_form.cleaned_data['email']
			)
			owner.AMPS_user = user
			owner.save()
	else:
		userdata_form = recordOwner()
		user_form = recordUser()

	return render(request, 'webapp/register.html', {'userdata_form': userdata_form, 'user_form' : user_form})

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
		#include here the user authentication 
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