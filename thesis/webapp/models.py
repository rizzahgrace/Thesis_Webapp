from django.db import models
from django.utils.timezone import now

# Create your models here.
class RawData(models.Model):
	winddir = models.IntegerField(null=True)
	windspeedmph = models.FloatField(null=True)
	windspdmph_avg2m = models.FloatField(null=True)
	rainin = models.FloatField(null=True)
	dailyrainin = models.FloatField(null=True)
	humidity = models.FloatField(null=True)
	tempf = models.FloatField(null=True)
	pressure = models.FloatField(null=True)
	timestamp = models.DateTimeField('date logged', default = now)

	def check_values(record):
		if (record.winddir >= 0):
			return True
		else:
			return False
