#all the commands were run in the python
import datetime
from django.contrib import messages
from .models import RawData_AMPS, RawData_Weather
import csv


def handle_upload_file(f, owner):
	dataReader=csv.reader(f.read().decode().splitlines(), delimiter=',', quotechar='"')
	for row in dataReader:
		datacsvweather=RawData_Weather()
		datacsvamps = RawData_AMPS()
		try:
			datacsvamps.grid = float(row[0])
		except(ValueError):
			datacsvamps.grid = None
		try:
			datacsvamps.load = float(row[1])
		except(ValueError):
			datacsvamps.load = None
		try:
			datacsvamps.batt_curr = float(row[2])
		except(ValueError):
			datacsvamps.batt_curr = None
		try:
			datacsvamps.batt_volt = float(row[3])
		except(ValueError):
			datacsvamps.batt_volt = None
		try:
			datacsvamps.SP_curr = float(row[4])
		except(ValueError):
			datacsvamps.SP_curr = None
		try:
			datacsvamps.SP_volt = float(row[5])
		except(ValueError):
			datacsvamps.SP_volt = None
		try:
			datacsvamps.SP_pow = (float(row[4])*float(row[5]))
		except(ValueError):
			datacsvamps.SP_pow = None
		
		try:
			datacsvweather.winddir = float(row[6])
		except(ValueError):
			datacsvweather.winddir = None
		try:
			datacsvweather.windspeedmph = (float(row[7])*1.6093440)
		except(ValueError):
			datacsvweather.windspeedmph = None
		try:
			datacsvweather.windspdmph_avg2m = float(row[8])
		except(ValueError):
			datacsvweather.windspdmph_avg2m = None
		try:
			datacsvweather.rainin = float(row[9])
		except(ValueError):
			datacsvweather.rainin = None
		try:
			datacsvweather.dailyrainin = float(row[10])
		except(ValueError):
			datacsvweather.dailyrainin = None
		try:
			datacsvweather.humidity = float(row[11])
		except(ValueError):
			datacsvweather.humidity = None
		try:
			datacsvweather.tempf = (((float(row[12])-32)*5)/9)
		except(ValueError):
			datacsvweather.tempf = None
		try:
			datacsvweather.pressure = float(row[13])
		except(ValueError):
			datacsvweather.pressure = None
		datacsvweather.timestamp=datetime.datetime.strptime(row[14], '%m/%d/%Y %H:%M')
		datacsvamps.timestamp=datetime.datetime.strptime(row[14], '%m/%d/%Y %H:%M')
		datacsvamps.owner = owner
		datacsvweather.save()
		datacsvamps.save()

# def historical_weather(self):
	