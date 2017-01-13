from django.http import HttpResponse
from django.shortcuts import render
from .models import RawData
from webapp.forms import UploadCSVFile
from webapp.utils import handle_upload_file
from django.contrib import messages
from highcharts.views import HighChartsBarView

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

class BarView(HighChartsBarView):
	categories = ['Orange', 'Bananas', 'Apples']

	@property
	def series(self):
		result = []
		for name in ('Joe', 'Jack', 'William', 'Averell'):
			data = []
			for x in range(len(self.categories)):
				data.append(random.randint(0, 10))
			result.append({'name': name, "data": data})
		return result