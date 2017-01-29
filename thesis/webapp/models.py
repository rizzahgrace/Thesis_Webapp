from django.db import models
from django.utils.timezone import now

# Create your models here.
class RawData(models.Model):
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
