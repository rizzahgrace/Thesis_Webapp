from django.contrib import admin
from .models import RawData

# Register your models here.
class RawDataAdmin(admin.ModelAdmin):
	fields = ['winddir', 'windspeedmph', 'windspdmph_avg2m', 'rainin', 'dailyrainin', 'humidity', 'tempf', 'pressure', 'timestamp']
	list_display = ('winddir','windspeedmph','rainin','timestamp')
	list_filter = ['timestamp']

# class SampleDataAdmin(admin.ModelAdmin):
# 	fields = ['month', 'sampledata']
# 	list_display = ('month','sampledata')
# 	list_filter = ['month']

admin.site.register(RawData, RawDataAdmin)
# admin.site.register(SampleData, SampleDataAdmin)