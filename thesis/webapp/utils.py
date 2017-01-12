#all the commands were run in the python
from django.contrib import messages
from .models import RawData
import csv
import datetime

def handle_upload_file(f):
	dataReader=csv.reader(f.read().decode().splitlines(), delimiter=',', quotechar='"')
	for row in dataReader:
		datacsv=RawData()
		try:
			datacsv.winddir = int(row[0])
		except(ValueError):
			datacsv.winddir = None
		try:
			datacsv.windspeedmph = float(row[1])
		except(ValueError):
			datacsv.windspeedmph = None
		try:
			datacsv.windspdmph_avg2m = float(row[2])
		except(ValueError):
			datacsv.windspdmph_avg2m = None
		try:
			datacsv.rainin = float(row[3])
		except(ValueError):
			datacsv.rainin = None
		try:
			datacsv.dailyrainin = float(row[4])
		except(ValueError):
			datacsv.dailyrainin = None
		try:
			datacsv.humidity = float(row[5])
		except(ValueError):
			datacsv.humidity = None
		try:
			datacsv.tempf = float(row[6])
		except(ValueError):
			datacsv.tempf = None
		try:
			datacsv.pressure = float(row[7])
		except(ValueError):
			datacsv.pressure = None
		datacsv.timestamp=datetime.datetime.strptime(row[8], '%d/%m/%Y %H:%M\t')
		datacsv.save()