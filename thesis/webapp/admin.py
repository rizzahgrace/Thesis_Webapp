from django.contrib import admin
from .models import RawData_Weather, RawData_AMPS

# Register your models here.
class RawDataWeatherAdmin(admin.ModelAdmin):
	fields = ['winddir', 'windspeedmph', 'windspdmph_avg2m', 'rainin', 'dailyrainin', 'humidity', 'tempf', 'pressure', 'timestamp']
	list_display = ('winddir', 'windspeedmph', 'windspdmph_avg2m', 'rainin', 'dailyrainin', 'humidity', 'tempf', 'pressure', 'timestamp')
	list_filter = ['timestamp']
	
class RawDataAMPSAdmin(admin.ModelAdmin):
	fields = ['grid', 'load', 'batt_curr', 'batt_volt', 'SP_curr', 'SP_volt', 'SP_pow', 'timestamp']
	list_display = ('grid', 'load', 'batt_curr', 'batt_volt', 'SP_curr', 'SP_volt', 'SP_pow', 'timestamp')
	list_filter = ['timestamp']

admin.site.register(RawData_Weather, RawDataWeatherAdmin)
admin.site.register(RawData_AMPS, RawDataAMPSAdmin)