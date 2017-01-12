from django.http import HttpResponse
from django.shortcuts import render
from .models import RawData
from webapp.forms import UploadCSVFile

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the webapp index.")

def csv(request):
	if request.method == 'POST':
		form = UploadCSVFile(request.POST, request.FILES)
		
		if form.is_valid():
			handle_upload_file(request.FILES['csvfile'])
			messages.success(request, 'Record saved')
	else:
		form = UploadCSVFile()

	return render(request, 'webapp/csv.html', {'form': form})