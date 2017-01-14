from django.contrib import admin
from .models import RawData

# Register your models here.
class RawDataAdmin(admin.ModelAdmin):
	fields = ['winddir', 'windspeedmph', 'windspdmph_avg2m', 'rainin', 'dailyrainin', 'humidity', 'tempf', 'pressure', 'timestamp']
	list_display = ('winddir','windspeedmph','rainin','timestamp')
	list_filter = ['timestamp']

admin.site.register(RawData, RawDataAdmin)