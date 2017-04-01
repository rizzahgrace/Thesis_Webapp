import datetime
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Case, Value, When
from .models import RawData_Weather, RawData_AMPS, Owner
from django.contrib.auth.models import User
from webapp.forms import UploadCSVFile, recordOwner, recordUser
from webapp.utils import handle_upload_file
from django.contrib import messages
from chartit import DataPool, Chart

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from webapp.serializers import DataSerializer, OwnerSerializer

from highcharts.views import (HighChartsMultiAxesView, HighChartsStockView)
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from webapp.permissions import IsAuthenticated

from rest_framework import generics, permissions, viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers

def loading(request):
	return render(request, 'webapp/loading.html')

def login_user(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/home/')
	else:
		return HttpResponseRedirect('/index/')
	return render_to_response('home.html', context_instance=RequestContext(request))

def index(request):
	return render(request, 'webapp/final/home.html')

def home(request):
	return render(request, 'webapp/final/home2.html')

def edits(request):
	return render(request, 'webapp/final/home3.html')

def weather(request):
	return render(request, 'webapp/final/weather.html')

def power(request):
	return render(request, 'webapp/final/power1.html')

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

	return render(request, 'webapp/final/register.html', {'userdata_form': userdata_form, 'user_form' : user_form})

def test_display(request):
	# processed_data = RawData_AMPS.objects.filter(AMPS_user=self.request.user).aggregate(Avg('load'))
	return render(request, 'webapp/index.html')#, processed_data)

class AdvancedGraph(HighChartsMultiAxesView):
	title = 'Weather Data'
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
		data = {'id': [], 'windspeedmph': [], 'temperature':[], 'timestamp':[]}
		f = RawData_Weather.objects.all()
		for unit in f:
			data['id'].append(unit.id)
			data['timestamp'].append(unit.timestamp.strftime('%I:%M'))
			data['windspeedmph'].append(unit.windspeedmph)
			data['temperature'].append(unit.tempf)


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
			'name': 'windspeedmph',
			'data': data['windspeedmph']
			},
			{
			'name': 'temperature',
			'data': data['temperature']
			} 
		]

		##### X LABELS
		# self.axis = data['id']
		

		##### SERIES WITH VALUES
		self.series = self.serie
		data = super(AdvancedGraph, self).get_data()
		return data
		
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
		data = {'id': [], 'load': [], 'SP_pow':[], 'timestamp':[]}
		f = RawData_AMPS.objects.all()[:10]
		for unit in f:
			data['id'].append(unit.id)
			data['timestamp'].append(unit.timestamp.strftime('%I:%M'))
			data['load'].append(unit.load)
			data['SP_pow'].append(unit.SP_pow)


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
			'name': 'Power Generated',
			'data': data['SP_pow']
			} 
		]

		##### X LABELS
		# self.axis = data['id']
		
		##### SERIES WITH VALUES
		self.series = self.serie
		data = super(PowerGraph, self).get_data()
		return data

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'owners': reverse('webapp:Owner-list', request=request, format=format),
		'AMPSdata': reverse('webapp:AMPSdata-list', request=request, format=format),	
		'mainmenu' : reverse('webapp:index', request=request, format=format)
	})


class AMPSdataView(APIView):
	permission_classes=(permissions.IsAuthenticated,)
	def get(self, request, format=None):
		if request.user.is_superuser:
			AMPSdata=RawData_AMPS.objects.all()
			serializer = DataSerializer(AMPSdata, many=True)
			return Response(serializer.data)
		else:
			user=self.request.user
			owner=user
			AMPSdata=RawData_AMPS.objects.filter(owner__AMPS_user=owner)
			serializer = DataSerializer(AMPSdata, many=True)
			return Response(serializer.data)


class OwnerView(APIView):
	permission_classes=(permissions.IsAuthenticated,)
	def get(self, request, format=None):
		if request.user.is_superuser:
			owners=Owner.objects.all()
			serializer = OwnerSerializer(owners, many=True)
			return Response(serializer.data)
		else:	
			user=self.request.user
			owner=user
			owners=Owner.objects.filter(AMPS_user=owner)
			serializer = OwnerSerializer(owners, many=True)
			return Response(serializer.data)

class UserList(generics.ListAPIView):
	queryset = Owner.objects.all()
	serializer_class = OwnerSerializer