from django.contrib import admin
from .models import RawData_Weather, RawData_AMPS, Owner

# Register your models here.
class RawDataWeatherAdmin(admin.ModelAdmin):
	fields = ['winddir', 'windspeedmph', 'windspdmph_avg2m', 'rainin', 'dailyrainin', 'humidity', 'tempf', 'pressure', 'timestamp', ]
	list_display = ('winddir', 'windspeedmph', 'windspdmph_avg2m', 'rainin', 'dailyrainin', 'humidity', 'tempf', 'pressure', 'timestamp')
	list_filter = ['timestamp']
	
class RawDataAMPSAdmin(admin.ModelAdmin):
	fields = ['grid', 'load', 'batt_curr', 'batt_volt', 'SP_curr', 'SP_volt', 'SP_pow', 'timestamp', 'owner']
	list_display = ('grid', 'load', 'batt_curr', 'batt_volt', 'SP_curr', 'SP_volt', 'SP_pow', 'timestamp', 'owner')
	list_filter = ['timestamp']

class OwnerAdmin(admin.ModelAdmin):
	fields = ['last_name', 'first_name', 'address', 'AMPS_user']
	list_display = ('last_name', 'first_name', 'address', 'AMPS_user')

admin.site.register(RawData_Weather, RawDataWeatherAdmin)
admin.site.register(RawData_AMPS, RawDataAMPSAdmin)
admin.site.register(Owner, OwnerAdmin)