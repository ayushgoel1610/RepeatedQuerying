from django.db import models
class Counter(models.Model):
	count = models.IntegerField(default=0)

class Halfhour(models.Model):
	device_id = models.IntegerField()
	time = models.DateTimeField()
	batch = models.CharField()
	count = models.IntegerField()

class Dailybasis(models.Model):
	device_id = models.IntegerField()
	day = models.DateTimeField()
	batch = models.CharField()
	count = models.IntegerField()

class Weeklybasis(models.Model):
	device_id = models.IntegerField()
	week = models.DateTimeField()
	batch = models.CharField()
	count = models.IntegerField()

class Monthlybasis(models.Model):
	device_id = models.IntegerField()
	month = models.DateTimeField()
	batch = models.CharField()
	count = models.IntegerField()

class Yearlybasis(models.Model):
	device_id = models.IntegerField()
	year = models.DateTimeField()
	batch = models.CharField()
	count = models.IntegerField()