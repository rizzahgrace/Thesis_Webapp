from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class RawData_Weather(models.Model):
	winddir = models.IntegerField()
	windspeedmph = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	windspdmph_avg2m = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	rainin = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	dailyrainin = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	humidity = models.DecimalField(max_digits=6, decimal_places=2, null=False)
	tempf = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	pressure = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	timestamp = models.DateTimeField('date logged', default = now)

	def check_values(record):
		if (record.winddir >= 0):
			return True
		else:
			return False

class RawData_AMPS(models.Model):
	grid = models.FloatField(null=True)
	load = models.FloatField(null=True)
	batt_curr = models.FloatField(null=True)
	batt_volt = models.FloatField(null=True)
	SP_curr = models.FloatField(null=True)
	SP_volt = models.FloatField(null=True)
	SP_pow = models.FloatField(null=True)
	timestamp = models.DateTimeField('date logged', default = now)
	AMPS_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
