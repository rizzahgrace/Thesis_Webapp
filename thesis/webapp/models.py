from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Owner(models.Model):
	last_name = models.CharField(max_length=50, unique=True)
	first_name = models.CharField(max_length=50)
	address = models.CharField(max_length=150)
	AMPS_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __unicode__(self):
		return self.last_name

	def __str__(self):
		return self.last_name
		
class RawData_Weather(models.Model):
	winddir = models.IntegerField()
	windspeedmph = models.FloatField(null=True)
	windspdmph_avg2m = models.FloatField(null=True)
	rainin = models.FloatField(null=True)
	dailyrainin = models.FloatField(null=True)
	humidity = models.FloatField(null=False)
	tempf = models.FloatField(null=True)
	pressure = models.FloatField(null=True)
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
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)


