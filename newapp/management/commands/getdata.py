from django.core.management.base import BaseCommand, CommandError

import json,csv
from django.shortcuts import render
from newapp.models import *
from time import strftime
from datetime import *
from dateutil.relativedelta import relativedelta
from django.http import HttpResponse

import pycurl
import StringIO

htmlsrc=""
time="2015-07-03-17:20:10"

class Command(BaseCommand):
#    args = '<poll_id poll_id ...>'
    help = 'Fetches the data from server and updates the database'

    def handle(self, *args, **options):
	
        d=datetime.now()-timedelta(minutes=30)
        d0=datetime.now()
        # d_half=d0-relativedelta(hours=-5,minutes=(d0.minute%30),seconds=d0.second,microseconds=d0.microsecond)
        from_time=d0-relativedelta(hours=-10,minutes=(d0.minute%30),seconds=d0.second,microseconds=d0.microsecond)
        fromtime=from_time.strftime("%Y-%m-%d-%H:%M:%S")
        to_time=from_time-relativedelta(minutes=-30)
        totime=to_time.strftime("%Y-%m-%d-%H:%M:%S")
        url = "https://192.168.1.40:9119/count?from="
        url = url+fromtime+"&to="
        url = url+totime+"&format=yyyy-mm-dd-hh24:mi:ss&token=98a4bafbb35b3527c524ac5d73e9ff8e5e56c6caed488b259682feb7d0a1d192"

        # response = urllib2.urlopen(url)
        #self.stdout.write("%s", url)
        # htmlsrc = response.read()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(pycurl.SSL_VERIFYHOST, 0)
        b = StringIO.StringIO()
        c.setopt(pycurl.WRITEFUNCTION, b.write)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.MAXREDIRS, 5)
        c.perform()
        htmlsrc = b.getvalue()

        json_data=htmlsrc
        data = json.loads(json_data)
        for i in range(0,len(data["counts"])):
            # d0=datetime.now()
            d_half=d0-relativedelta(hours=-5,minutes=(d0.minute%30),seconds=d0.second,microseconds=d0.microsecond)
            halfhourlybasis_new = Halfhour(device_id=data["counts"][i]["device_id"],time=d_half, batch=data["counts"][i]["batch"], count=data["counts"][i]["count"])
            halfhourlybasis_new.save()

            # d1=d0-timedelta(days=1)
            today = d_half-relativedelta(hours=d_half.hour+5,minutes=d_half.minute,seconds=d_half.second,microseconds=d_half.microsecond)
            # print today
            try:
                dailybasis_last = Dailybasis.objects.get(device_id=data["counts"][i]["device_id"],batch=data["counts"][i]["batch"],day=today)
            # print dailybasis_last
            except:
                # print "in except block daywise"
                dailybasis_last = None
            if  dailybasis_last is not None:
                if  dailybasis_last.day.replace(tzinfo=None)<d0:
                    # print str(dailybasis_last.count) +"+"+(data["counts"][i]["count"])
                    # dailybasis_last_obj = dailybasis_last.latest("day")
                    # dailybasis_last_obj = dailybasis_last[0]
                    count1=dailybasis_last.count
                    dailybasis_last.count=count1+long(data["counts"][i]["count"])
                   # if dailybasis_last.save(update_fields=["count"]):
                       # print "true!"
                    #else:
                       # print "false!"
                    # dailybasis_last_obj.count = dailybasis_last_obj.count + long(data["counts"][i]["count"])
                    # if dailybasis_last_obj.save()
                    # 	print "true"
                    # else
                    # 	print "why :/"
                    # print dailybasis_last[dailybasis_last_len-1]
            else:
                dailybasis_new = Dailybasis(device_id=data["counts"][i]["device_id"],day=today, batch=data["counts"][i]["batch"], count=data["counts"][i]["count"])
                dailybasis_new.save()

            # d2=d0-timedelta(days=7)
            # try:
            # 	weeklybasis_last = Weeklybasis.objects.filter(device_id=data["counts"][i]["device_id"],batch=data["counts"][i]["batch"]).order_by("week")
            # 	weeklybasis_last_len = weeklybasis_last.count()
            # 	print weeklybasis_last
            # except:
            # 	print "in except block weekwise"
            # 	weeklybasis_last = None
            # if  weeklybasis_last is not None and weeklybasis_last_len>0:
            # 	if  weeklybasis_last[weeklybasis_last_len-1].week.replace(tzinfo=None)>d2:
            # 		weeklybasis_last[weeklybasis_last_len-1].count = weeklybasis_last[weeklybasis_last_len-1].count + long(data["counts"][i]["count"])
            # 		weeklybasis_last[weeklybasis_last_len-1].save()
            # else:
            # 	weeklybasis_new = Weeklybasis(device_id=data["counts"][i]["device_id"],week=d, batch=data["counts"][i]["batch"], count=data["counts"][i]["count"])
            # 	weeklybasis_new.save()
            d3=d_half-relativedelta(days=d_half.day,hours=d_half.hour+5,minutes=d_half.minute,seconds=d_half.second,microseconds=d_half.microsecond)
           # print d3
            try:
                monthlybasis_last = Monthlybasis.objects.get(device_id=data["counts"][i]["device_id"],batch=data["counts"][i]["batch"],month=d3)
            # print monthlybasis_last
            # monthlybasis_last_len = monthlybasis_last.count()
            # print monthlybasis_last_len
            except:
                # print "in except block monthwise"
                monthlybasis_last = None
            if monthlybasis_last is not None:
                if  monthlybasis_last.month.replace(tzinfo=None)<d0:
                    monthlybasis_last.count = monthlybasis_last.count + long(data["counts"][i]["count"])
                    monthlybasis_last.save()
            else:
                monthlybasis_new = Monthlybasis(device_id=data["counts"][i]["device_id"],month=d3, batch=data["counts"][i]["batch"], count=data["counts"][i]["count"])
                monthlybasis_new.save()
            d4=d_half-relativedelta(months=d_half.month,days=d_half.day,hours=d_half.hour+5,minutes=d_half.minute,seconds=d_half.second,microseconds=d_half.microsecond)
            try:
                yearlybasis_last = Yearlybasis.objects.get(device_id=data["counts"][i]["device_id"],batch=data["counts"][i]["batch"],year=d4)
            # yearlybasis_last_len = yearlybasis_last.count()
            # print yearlybasis_last_len
            except:
            #    print "in except block yearwise"
                yearlybasis_last = None
            if yearlybasis_last is not None:
                if  yearlybasis_last.year.replace(tzinfo=None)<d0:
                    yearlybasis_last.count = yearlybasis_last.count + long(data["counts"][i]["count"])
                    yearlybasis_last.save()
            else:
                yearlybasis_new = Yearlybasis(device_id=data["counts"][i]["device_id"],year=d4, batch=data["counts"][i]["batch"], count=data["counts"][i]["count"])
                yearlybasis_new.save()
