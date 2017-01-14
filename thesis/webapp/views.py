from django.http import HttpResponse
from django.shortcuts import render
from .models import RawData
from webapp.forms import UploadCSVFile
from webapp.utils import handle_upload_file
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'rawdata': reverse('webapp:rawdata', request=request, format=format),
    })
class RawDataView(APIView):
    def get(self, request, format=None):
    	rawdata=RawData.objects.all()
    	serializer = DataSerializer(rawdata, many=True)
    	return Response(serializer.data)