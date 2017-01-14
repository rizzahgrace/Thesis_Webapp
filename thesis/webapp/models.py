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

def enrollment_chart(self):
	lu = { 'categories' : [ 'Fall 2008', 'Spring 2009','Fall 2009', 'Spring 2010', 'Fall 2010', 'Spring 2011'],
		'undergrad' : [18, 22, 30, 3, 40, 47],
		'grad' : [1, 2, 4, 4, 5, 7],
		'employee' : [2, 3, 0, 1, 1, 2] }
	lu['total_enrolled'] = [sum(a) for a in zip(lu['undergrad'], lu['grad'],lu['employee'])]
	return render_to_string('webapp/templates/webapp/home.html', lu )
	enrollment_chart.allow_tags = True