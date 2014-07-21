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
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

# def countapi(request):
# 	d=datetime.now()-timedelta(minutes=30)
# 	fromtime=d.strftime("%Y-%m-%d-%H:%M:%S")
# 	totime=strftime("%Y-%m-%d-%H:%M:%S")
# 	url = "https://192.168.1.40:9119/count?from="
# 	url = url+fromtime+"&to="
# 	url = url+totime+"&format=yyyy-mm-dd-hh24:mi:ss&token=98a4bafbb35b3527c524ac5d73e9ff8e5e56c6caed488b259682feb7d0a1d192"
# 	response = urllib2.urlopen(url)
# 	htmlsrc = response.read()
# 	json_data=htmlsrc
# 	data = json.loads(json_data)
# 	for i in range(0,len(data["counts"])):
# 		halfhourlybasis_new = Halfhour(device_id=data["counts"][i]["device_id"],time=d, batch=data["counts"][i]["batch"], count=data["counts"][i]["count"])
# 		halfhourlybasis_new.save()
# 		d0=datetime.now()
# 		d1=d0-timedelta(days=1)
# 		try:
# 			dailybasis_last = Dailybasis.objects.filter(device_id=data["counts"][i]["device_id"],batch=data["counts"][i]["batch"]).order_by("day").reverse()
# 			dailybasis_last_len = dailybasis_last.count()
# 			print dailybasis_last
# 		except:
# 			print "in except block daywise"
# 			dailybasis_last = None
# 		if  dailybasis_last is not None and dailybasis_last_len>0:
# 			if  dailybasis_last[0].day.replace(tzinfo=None)>d1:
# 				print str(dailybasis_last[0].count) +"+"+(data["counts"][i]["count"])
# 				# dailybasis_last_obj = dailybasis_last.latest("day")
# 				dailybasis_last_obj = dailybasis_last[0]
# 				count1=dailybasis_last_obj.count
# 				dailybasis_last_obj.update(count=count1+long(data["counts"][i]["count"]))
# 				# dailybasis_last_obj.count = dailybasis_last_obj.count + long(data["counts"][i]["count"])
# 				# if dailybasis_last_obj.save()
# 				# 	print "true"
# 				# else
# 				# 	print "why :/"
# 				# print dailybasis_last[dailybasis_last_len-1]
# 		else:
# 			dailybasis_new = Dailybasis(device_id=data["counts"][i]["device_id"],day=d, batch=data["counts"][i]["batch"], count=data["counts"][i]["count"])
# 			dailybasis_new.save()

# 		d2=d0-timedelta(days=7)
# 		try:
# 			weeklybasis_last = Weeklybasis.objects.filter(device_id=data["counts"][i]["device_id"],batch=data["counts"][i]["batch"]).order_by("week")
# 			weeklybasis_last_len = weeklybasis_last.count()
# 			print weeklybasis_last
# 		except:
# 			print "in except block weekwise"
# 			weeklybasis_last = None
# 		if  weeklybasis_last is not None and weeklybasis_last_len>0:
# 			if  weeklybasis_last[weeklybasis_last_len-1].week.replace(tzinfo=None)>d2:
# 				weeklybasis_last[weeklybasis_last_len-1].count = weeklybasis_last[weeklybasis_last_len-1].count + long(data["counts"][i]["count"])
# 				weeklybasis_last[weeklybasis_last_len-1].save()
# 		else:
# 			weeklybasis_new = Weeklybasis(device_id=data["counts"][i]["device_id"],week=d, batch=data["counts"][i]["batch"], count=data["counts"][i]["count"])
# 			weeklybasis_new.save()
# 		d3=d0-relativedelta(months=1)
# 		try:
# 			monthlybasis_last = Monthlybasis.objects.filter(device_id=data["counts"][i]["device_id"],batch=data["counts"][i]["batch"]).order_by("month")
# 			monthlybasis_last_len = monthlybasis_last.count()
# 			print monthlybasis_last_len
# 		except:
# 			print "in except block monthwise"
# 			monthlybasis_last = None
# 		if monthlybasis_last is not None and monthlybasis_last_len>0:
# 			if  monthlybasis_last[monthlybasis_last_len-1].month.replace(tzinfo=None)>d3:
# 				monthlybasis_last[monthlybasis_last_len-1].count = monthlybasis_last[monthlybasis_last_len-1].count + long(data["counts"][i]["count"])
# 				monthlybasis_last[monthlybasis_last_len-1].save()
# 		else:
# 			monthlybasis_new = Monthlybasis(device_id=data["counts"][i]["device_id"],month=d, batch=data["counts"][i]["batch"], count=data["counts"][i]["count"])
# 			monthlybasis_new.save()
# 		d4=d0-relativedelta(years=7)
# 		try:
# 			yearlybasis_last = Yearlybasis.objects.filter(device_id=data["counts"][i]["device_id"],batch=data["counts"][i]["batch"]).order_by("year")
# 			yearlybasis_last_len = yearlybasis_last.count()
# 			print yearlybasis_last_len
# 		except:
# 			print "in except block yearwise"
# 			yearlybasis_last = None
# 		if yearlybasis_last is not None and yearlybasis_last_len>0:
# 			if  yearlybasis_last[yearlybasis_last_len-1].year.replace(tzinfo=None)>d4:
# 				yearlybasis_last[yearlybasis_last_len-1].count = yearlybasis_last[yearlybasis_last_len-1].count + long(data["counts"][i]["count"])
# 				yearlybasis_last[yearlybasis_last_len-1].save()
# 		else:
# 			yearlybasis_new = Yearlybasis(device_id=data["counts"][i]["device_id"],year=d, batch=data["counts"][i]["batch"], count=data["counts"][i]["count"])
# 			yearlybasis_new.save()
# 	return render(request, 'demoapp2/count.html',{'htmlsrc': htmlsrc})

def countapi(request):
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
    print url
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
                if dailybasis_last.save(update_fields=["count"]):
                    print "true!"
                else:
                    print "false!"
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
        print d3
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
            print "in except block yearwise"
            yearlybasis_last = None
        if yearlybasis_last is not None:
            if  yearlybasis_last.year.replace(tzinfo=None)<d0:
                yearlybasis_last.count = yearlybasis_last.count + long(data["counts"][i]["count"])
                yearlybasis_last.save()
        else:
            yearlybasis_new = Yearlybasis(device_id=data["counts"][i]["device_id"],year=d4, batch=data["counts"][i]["batch"], count=data["counts"][i]["count"])
            yearlybasis_new.save()
    return render(request, 'demoapp2/count.html',{'htmlsrc': htmlsrc})

# starttime=datetime.now()
def countapi_old(starttime):
    # global starttime
    d=datetime.now()-timedelta(minutes=30)
    d0=starttime
    # d_half=d0-relativedelta(hours=-5,minutes=(d0.minute%30),seconds=d0.second,microseconds=d0.microsecond)
    from_time=d0-relativedelta(hours=-10,minutes=(d0.minute%30),seconds=d0.second,microseconds=d0.microsecond)
    fromtime=from_time.strftime("%Y-%m-%d-%H:%M:%S")
    to_time=from_time-relativedelta(minutes=-30)
    totime=to_time.strftime("%Y-%m-%d-%H:%M:%S")
    url = "https://192.168.1.40:9119/count?from="
    url = url+fromtime+"&to="
    url = url+totime+"&format=yyyy-mm-dd-hh24:mi:ss&token=98a4bafbb35b3527c524ac5d73e9ff8e5e56c6caed488b259682feb7d0a1d192"
    # response = urllib2.urlopen(url)
    # starttime=totime
    print url
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
                if dailybasis_last.save(update_fields=["count"]):
                    print "true!"
                else:
                    print "false!"
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
        print d3
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
            print "in except block yearwise"
            yearlybasis_last = None
        if yearlybasis_last is not None:
            if  yearlybasis_last.year.replace(tzinfo=None)<d0:
                yearlybasis_last.count = yearlybasis_last.count + long(data["counts"][i]["count"])
                yearlybasis_last.save()
        else:
            yearlybasis_new = Yearlybasis(device_id=data["counts"][i]["device_id"],year=d4, batch=data["counts"][i]["batch"], count=data["counts"][i]["count"])
            yearlybasis_new.save()

    # return render(request, 'demoapp2/count.html',{'htmlsrc': htmlsrc})


def fetch_old(request,dt1,dt2):
    global starttime
    starttime=datetime.strptime(dt1,"%Y-%m-%d %H:%M:%S")
    endtime=datetime.strptime(dt2,"%Y-%m-%d %H:%M:%S")
    while starttime<endtime:
        countapi_old(starttime)
        starttime=starttime+relativedelta(minutes=30)

# def halfhour_particularday(request,time1,time2,month):
#     d1=time1
#     d2=time2
#     date1=datetime.strptime(d1,"%Y-%m-%d %H:%M:%S")
#     days1=date1.day
#     month_diff1=date1.month-month
#     date2=datetime.strptime(d2,"%Y-%m-%d %H:%M:%S")
#     days2=date2.day
#     month_diff2=date2.month-month
#     date1=date1-relativedelta(months=month_diff1,hours=5)
#     date2=date2-relativedelta(months=month_diff2,hours=5)
#     startofmonth
    
def halfhour_particularday(request,day,dt1,dt2):
    date=datetime.strptime(dt1,"%Y-%m-%d")#(year=int(year),month=int(month),day=1)
    date1=date-relativedelta(hours=5)
    list=[]
    # while date1.month != month+1:
    # objects= Halfhour.objects.filter(time=date1)
    while (date1+relativedelta(hours=5)).strftime("%A") != day:
        #date1=datetime(year=date1.year,month=date1.month,day=date1.day+1,hour=date1.hour,minute=date1.minute,second=date1.second,microsecond=date1.microsecond)
        date1=date1+relativedelta(days=1)
    datedt2=datetime.strptime(dt2,"%Y-%m-%d")
    date2=date1
    date1_print=date1
    count_of_weeks=0
    while (date2.day<=datedt2.day and date2.month<=datedt2.month) or (date2.month<datedt2.month):#(date2+relativedelta(hours=5)).month != int(month)+1:
        count_of_weeks=count_of_weeks+1
        # date2=datetime(year=date2.year,month=date2.month,day=date2.day+7,hour=date2.hour,minute=date2.minute,second=date2.second,microsecond=date2.microsecond)
        date2=date2+relativedelta(days=7)
    # date2=datetime(year=date2.year,month=date2.month,day=date2.day-7,hour=date2.hour,minute=date2.minute,second=date2.second,microsecond=date2.microsecond)
    # date2=date2-relativedelta(days=7)
    date2_print=date2
    list=[]
    i=0
    while i<49:
        i=i+1
        objects= Halfhour.objects.filter(time=date1)
        for o in objects:
            dic={}
            dic["time"]=o.time.time()
            dic["count"]=o.count
            dic["batch"]=o.batch
            dic["device_id"]=o.device_id
            list.append(dic)
        date1 = date1 +relativedelta(minutes=30)
    date1 = date1 + relativedelta(days=6)
    while not (date1.day == date2.day and date1.month == date2.month):
        i=0
        while i<49:
            i=i+1
            objects= Halfhour.objects.filter(time=date1)
            for o in objects:
                status=0
                for l in list:
                    
                    if l["time"]==o.time.time() and l["batch"]==o.batch and l["device_id"]==o.device_id:
                        status=1
                        l["count"]=l["count"]+o.count
                if status==0:
                    dic={}
                    dic["time"]=o.time.time()
                    dic["count"]=o.count
                    dic["batch"]=o.batch
                    dic["device_id"]=o.device_id
                    list.append(dic)
            date1 = date1 +relativedelta(minutes=30)
        date1=date1 + relativedelta(days=6)
    keys = ['time','device_id', 'batch', 'count']
    # f = open('buildingwise.csv', 'wb')
    # dict_writer = csv.DictWriter(f, keys)
    # dict_writer.writer.writerow(keys)
    # dict_writer.writerows(data["log entries"])
    print "count:"
    print count_of_weeks
    print date2
    print "print"
    print date1_print
    print date2_print
    for d in list:
        d["count"]=d["count"]/(float(count_of_weeks))
    response1 = HttpResponse(content_type='text/csv')
    response1['Content-Disposition'] = 'attachment; filename="halfhour_particularday.csv"'
    dict_writer = csv.DictWriter(response1, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(list)
    # writer = csv.writer(response)
    #    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response1


def halfhour_any_month(request,dt1,dt2):
    date=datetime.strptime(dt1,"%Y-%m-%d")#(year=int(year),month=int(month),day=1)
    date1=date-relativedelta(hours=5)
    list=[]
    # date2=date+relativedelta(months=1)
    # d_iter=date1
    # while date1.month != month+1:
    # objects= Halfhour.objects.filter(time=date1)
    # while d_iter.month==d.month:

    #     objects= Dailybasis.objects.filter(time=d_iter)

    #     for o in objects:
    #         dic={}
    #         dic["time"]=o.day
    #         dic["count"]=o.count
    #         dic["batch"]=o.batch
    #         dic["device_id"]=o.device_id
    #         list.append(dic)
    #     d_iter=d_iter+relativedelta(days=1)

    # while (date1+relativedelta(hours=5)).strftime("%A") != day:
    #     #date1=datetime(year=date1.year,month=date1.month,day=date1.day+1,hour=date1.hour,minute=date1.minute,second=date1.second,microsecond=date1.microsecond)
    #     date1=date1+relativedelta(days=1)
    datedt2=datetime.strptime(dt2,"%Y-%m-%d")
    date2=date1
    count_of_days=0
    while (date2.day<=datedt2.day and date2.month<=datedt2.month) or (date2.month<datedt2.month):#(date2+relativedelta(hours=5)).month != int(date.month)+1:
        count_of_days=count_of_days+1
        # date2=datetime(year=date2.year,month=date2.month,day=date2.day+7,hour=date2.hour,minute=date2.minute,second=date2.second,microsecond=date2.microsecond)
        date2=date2+relativedelta(days=1)
    # date2=datetime(year=date2.year,month=date2.month,day=date2.day-7,hour=date2.hour,minute=date2.minute,second=date2.second,microsecond=date2.microsecond)
    list=[]
    i=0
    while i<49:
        i=i+1
        objects= Halfhour.objects.filter(time=date1)
        for o in objects:
            dic={}
            dic["time"]=o.time.time()
            dic["count"]=o.count
            dic["batch"]=o.batch
            dic["device_id"]=o.device_id
            list.append(dic)
        date1 = date1 +relativedelta(minutes=30)
    # date1 = date1 + relativedelta(days=6)
    while not(date1.day == date2.day and date1.month == date2.month):
        i=0
        while i<49:
            i=i+1
            objects= Halfhour.objects.filter(time=date1)
            for o in objects:
                status=0
                for l in list:
                    
                    if l["time"]==o.time.time() and l["batch"]==o.batch and l["device_id"]==o.device_id:
                        status=1
                        l["count"]=l["count"]+o.count
                if status==0:
                    dic={}
                    dic["time"]=o.time.time()
                    dic["count"]=o.count
                    dic["batch"]=o.batch
                    dic["device_id"]=o.device_id
                    list.append(dic)
            date1 = date1 +relativedelta(minutes=30)
        # date1=date1 + relativedelta(days=6)
    keys = ['time','device_id', 'batch', 'count']
    # f = open('buildingwise.csv', 'wb')
    # dict_writer = csv.DictWriter(f, keys)
    # dict_writer.writer.writerow(keys)
    # dict_writer.writerows(data["log entries"])
    print "count:"
    print count_of_days
    print date2
    for d in list:
        d["count"]=d["count"]/(float(count_of_days))
    response1 = HttpResponse(content_type='text/csv')
    response1['Content-Disposition'] = 'attachment; filename="halfhour_any_month.csv"'
    dict_writer = csv.DictWriter(response1, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(list)
    # writer = csv.writer(response)
    #    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response1

def halfhour_any_week(request,week,month,year,t11,t12):
    date=datetime(year=int(year),month=int(month),day=1)
    date1=date-relativedelta(hours=5)
    list=[]
    t1=datetime.strptime(t11,"%H:%M:%S")
    t2=datetime.strptime(t12,"%H:%M:%S")
    # date2=date+relativedelta(months=1)
    # d_iter=date1
    # while date1.month != month+1:
    # objects= Halfhour.objects.filter(time=date1)
    # while d_iter.month==d.month:

    #     objects= Dailybasis.objects.filter(time=d_iter)

    #     for o in objects:
    #         dic={}
    #         dic["time"]=o.day
    #         dic["count"]=o.count
    #         dic["batch"]=o.batch
    #         dic["device_id"]=o.device_id
    #         list.append(dic)
    #     d_iter=d_iter+relativedelta(days=1)

    while (date1+relativedelta(hours=5)).strftime("%A") != "Monday":
        # print (date1+relativedelta(hours=5)).strftime("%A")
        # print (date1+relativedelta(hours=5)).strftime("%A") != "Monday"
        #date1=datetime(year=date1.year,month=date1.month,day=date1.day+1,hour=date1.hour,minute=date1.minute,second=date1.second,microsecond=date1.microsecond)
        date1=date1+relativedelta(days=1)
    print "hi"
    week_no =1
    while week_no<int(week) and date1.day<28:
        week_no=week_no+1
        date1=date1+relativedelta(days=7)
    print "hi1"
    date2=date1
    count_of_days=0
    date1_print=date1
    while (date2+relativedelta(hours=5)).day != (date1+relativedelta(days=7)).day:
        count_of_days=count_of_days+1
        # date2=datetime(year=date2.year,month=date2.month,day=date2.day+7,hour=date2.hour,minute=date2.minute,second=date2.second,microsecond=date2.microsecond)
        date2=date2+relativedelta(days=1)
    # date2=datetime(year=date2.year,month=date2.month,day=date2.day-7,hour=date2.hour,minute=date2.minute,second=date2.second,microsecond=date2.microsecond)
    print "hi2"
    list=[]
    i=0
    no_of_half_hour=0
    while i<49:
        i=i+1
        if (date1+relativedelta(hours=5)).time()>=t1.time() and (date1+relativedelta(hours=5)).time()<t2.time(): 
            no_of_half_hour=no_of_half_hour+1
            objects= Halfhour.objects.filter(time=date1)
            for o in objects:
                dic={}
                dic["time"]=o.time.date()
                dic["count"]=o.count
                dic["batch"]=o.batch
                dic["device_id"]=o.device_id
                list.append(dic)
        date1 = date1 +relativedelta(minutes=30)
    print "hi3"
    # date1 = date1 + relativedelta(days=6)
    while date1.day != date2.day:
        i=0
        while i<49:
            i=i+1
            if (date1+relativedelta(hours=5)).time()>=t1.time() and (date1+relativedelta(hours=5)).time()<t2.time():
                objects= Halfhour.objects.filter(time=date1)
                for o in objects:
                    status=0
                    for l in list:
                        
                        if l["time"]==o.time.date() and l["batch"]==o.batch and l["device_id"]==o.device_id:
                            status=1
                            l["count"]=l["count"]+o.count
                    if status==0:
                        dic={}
                        dic["time"]=o.time.date()
                        dic["count"]=o.count
                        dic["batch"]=o.batch
                        dic["device_id"]=o.device_id
                        list.append(dic)
            date1 = date1 +relativedelta(minutes=30)
        # date1=date1 + relativedelta(days=6)
    print "hi4"
    keys = ['time','device_id', 'batch', 'count']
    # f = open('buildingwise.csv', 'wb')
    # dict_writer = csv.DictWriter(f, keys)
    # dict_writer.writer.writerow(keys)
    # dict_writer.writerows(data["log entries"])
    print "count:"
    print count_of_days
    print date2
    print date1_print
    for d in list:
        d["count"]=d["count"]/(float(no_of_half_hour))
    response1 = HttpResponse(content_type='text/csv')
    response1['Content-Disposition'] = 'attachment; filename="halfhour_any_week.csv"'
    dict_writer = csv.DictWriter(response1, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(list)
    # writer = csv.writer(response)
    #    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response1
def halfhour_single(request,param):
    # d contains the string for date in the specified format
    d=param
    time1=datetime.strptime(d,"%Y-%m-%d %H:%M:%S")-relativedelta(hours=5)
    objects= Halfhour.objects.filter(time=time1)
    list=[]
    for o in objects:
        dic={}
        dic["count"]=o.count
        dic["batch"]=o.batch
        dic["device_id"]=o.device_id
        dic["time"]=o.time
        list.append(dic)
    keys = [ 'time','count', 'batch','device_id']
    # f = open('buildingwise.csv', 'wb')
    # dict_writer = csv.DictWriter(f, keys)
    # dict_writer.writer.writerow(keys)
    # dict_writer.writerows(data["log entries"])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'filename="buildingwise.csv"'
    dict_writer = csv.DictWriter(response, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(list)
    # writer = csv.writer(response)
    #    writer.writerow(['device_id', 'batch', 'count'])
    # 	  for i in range (0,len(lis)):
    #    		writer.writerow([list[i]["device_id"], list[i]["batch"], list[i]["count"]])
    return response

def halfhour_day(request,param):
    # d1 contains the string for date in the specified format
    d1=param
    d=datetime.strptime(d1,"%Y-%m-%d %H:%M:%S")
    time1=d-relativedelta(hours=d.hour+5,minutes=d.minute,seconds=d.second,microseconds=d.microsecond)
    nextdaytime=d-relativedelta(days=-1,hours=d.hour+5,minutes=d.minute,seconds=d.second,microseconds=d.microsecond)
    d_iter=time1
    list=[]
    while d_iter.day == d.day:
        objects= Halfhour.objects.filter(time=d_iter)

        for o in objects:
            dic={}
            dic["time"]=o.time
            dic["count"]=o.count
            dic["batch"]=o.batch
            dic["device_id"]=o.device_id
            list.append(dic)
        d_iter = d_iter +relativedelta(minutes=30)
    keys = ['time','device_id', 'batch', 'count']
    # f = open('buildingwise.csv', 'wb')
    # dict_writer = csv.DictWriter(f, keys)
    # dict_writer.writer.writerow(keys)
    # dict_writer.writerows(data["log entries"])

    response1 = HttpResponse(content_type='text/csv')
    response1['Content-Disposition'] = 'attachment; filename="halfhour_day.csv"'
    dict_writer = csv.DictWriter(response1, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(list)
    # writer = csv.writer(response)
    #    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response1


def day_single(request,param):
    # d1 contains the string for date in the specified format
    d1=param
    d=datetime.strptime(d1,"%Y-%m-%d %H:%M:%S")
    time1=d-relativedelta(hours=5+d.hour,minutes=d.minute,seconds=d.second,microseconds=d.microsecond)
    nextdaytime=d-relativedelta(days=-1,hours=5+d.hour,minutes=d.minute,seconds=d.second,microseconds=d.microsecond)
    objects= Dailybasis.objects.filter(day=time1)
    list=[]
    for o in objects:
        dic={}
        dic["time"]=o.day
        dic["count"]=o.count
        dic["batch"]=o.batch
        dic["device_id"]=o.device_id
        list.append(dic)
    keys = ['time','device_id', 'batch', 'count']
    # f = open('buildingwise.csv', 'wb')
    # dict_writer = csv.DictWriter(f, keys)
    # dict_writer.writer.writerow(keys)
    # dict_writer.writerows(data["log entries"])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="day_single.csv"'
    dict_writer = csv.DictWriter(response, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(list)
    # writer = csv.writer(response)
    #    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response

def day_month(request,param):
    # d1 contains the string for date in the specified format
    d1=param
    d=datetime.strptime(d1,"%Y-%m-%d %H:%M:%S")
    time1=d-relativedelta(hours=5+d.hour,minutes=d.minute,seconds=d.second,microseconds=d.microsecond)
    nextdaytime=d-relativedelta(days=-1,hours=5+d.hour,minutes=d.minute,seconds=d.second,microseconds=d.microsecond)
    d_iter=time1
    list=[]
    while d_iter.month==d.month:

        objects= Dailybasis.objects.filter(day=d_iter)

        for o in objects:
            dic={}
            dic["time"]=o.day
            dic["count"]=o.count
            dic["batch"]=o.batch
            dic["device_id"]=o.device_id
            list.append(dic)
        d_iter=d_iter+relativedelta(days=1)
    keys = ['time','device_id', 'batch', 'count']
    # f = open('buildingwise.csv', 'wb')
    # dict_writer = csv.DictWriter(f, keys)
    # dict_writer.writer.writerow(keys)
    # dict_writer.writerows(data["log entries"])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="day_month.csv"'
    dict_writer = csv.DictWriter(response, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(list)
    # writer = csv.writer(response)
    #    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response

def day_custom(request,d1,d2):
    # d1 contains the string for date in the specified format
    
    d=datetime.strptime(d1,"%Y-%m-%d")
    time1=d-relativedelta(hours=5)
    d_end=datetime.strptime(d2,"%Y-%m-%d")
    end_date=d_end-relativedelta(hours=5)
    d_iter=time1
    count_dict={}
    list=[]
    while (d_iter.day<=end_date.day and d_iter.month<=end_date.month) or (d_iter.month<end_date.month):

        objects= Dailybasis.objects.filter(day=d_iter)
        if count_dict.get(d_iter.strftime("%A")) != None:
            count_dict[d_iter.strftime("%A")]=count_dict[d_iter.strftime("%A")]+1
        else:
            count_dict[d_iter.strftime("%A")]=1
        for o in objects:
            status=0
            for l in list:
                
                if l["time"]==o.day.strftime("%A") and l["batch"]==o.batch and l["device_id"]==o.device_id:
                    status=1
                    l["count"]=l["count"]+o.count
            if status==0:
                dic={}
                dic["time"]=o.day.strftime("%A")
                dic["count"]=o.count
                dic["batch"]=o.batch
                dic["device_id"]=o.device_id
                list.append(dic)
        d_iter=d_iter+relativedelta(days=1)

    keys = ['time','device_id', 'batch', 'count']
    # f = open('buildingwise.csv', 'wb')
    # dict_writer = csv.DictWriter(f, keys)
    # dict_writer.writer.writerow(keys)
    # dict_writer.writerows(data["log entries"])
    for d in list:
        d["count"]=d["count"]/(float(count_dict[d["time"]]))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="day_custom.csv"'
    dict_writer = csv.DictWriter(response, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(list)
    # writer = csv.writer(response)
    #    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response



def month_single(request,param):
    # d1 contains the string for date in the specified format
    d1=param
    d=datetime.strptime(d1,"%Y-%m-%d %H:%M:%S")
    time1=d-relativedelta(days=d.day,hours=5+d.hour,minutes=d.minute,seconds=d.second,microseconds=d.microsecond)
    # nextdaytime=d-relativedelta(days=-1,hours=d.hour,minutes=d.minute,seconds=d.second,microseconds=d.microsecond)
    # d_iter=time1
    list=[]

    objects= Monthlybasis.objects.filter(month=time1)

    for o in objects:
        dic={}
        dic["time"]=o.month
        dic["count"]=o.count
        dic["batch"]=o.batch
        dic["device_id"]=o.device_id
        list.append(dic)
    keys = ['time','device_id', 'batch', 'count']
    # f = open('buildingwise.csv', 'wb')
    # dict_writer = csv.DictWriter(f, keys)
    # dict_writer.writer.writerow(keys)
    # dict_writer.writerows(data["log entries"])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="month_single.csv"'
    dict_writer = csv.DictWriter(response, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(list)
    # writer = csv.writer(response)
    #    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response

def month_year(request,param):
    # d1 contains the string for date in the specified format
    d1=param
    d=datetime.strptime(d1,"%Y-%m-%d %H:%M:%S")
    time1=d-relativedelta(months=d.month-1,days=d.day-1,hours=d.hour+5,minutes=d.minute,seconds=d.second,microseconds=d.microsecond)
    yearaftertime=d+relativedelta(years=1)
    d_iter=time1
    print "d_iter:"
    print d_iter
    print "d:"
    print d
    list=[]
    count=0
    while d_iter.year!=yearaftertime.year:

        objects= Monthlybasis.objects.filter(month=d_iter)
        count+=1
        for o in objects:
            dic={}
            dic["time"]=o.month
            dic["count"]=o.count
            dic["batch"]=o.batch
            dic["device_id"]=o.device_id
            list.append(dic)
        d_iter = d_iter +relativedelta(months=1)
        if(d_iter.month==3):
            d_iter = d_iter + relativedelta(days=1)
    keys = ['time','device_id', 'batch', 'count']
    # f = open('buildingwise.csv', 'wb')
    # dict_writer = csv.DictWriter(f, keys)
    # dict_writer.writer.writerow(keys)
    # dict_writer.writerows(data["log entries"])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="month_year.csv"'
    dict_writer = csv.DictWriter(response, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(list)
    # writer = csv.writer(response)
    #    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response

def try1(request,change):
    print change
    print type(str(change))
    return HttpResponse(str(change))

def index(request):
    #counterget = Counter.objects.all()[:1].get()
    #countget = counterget.count
    #countget = countget + 1
    #counterget.count = countget
    #counterget.save()

    global htmlsrc,time
    d=datetime.now()-timedelta(minutes=30)
    fromtime=d.strftime("%Y-%m-%d-%H:%M:%S")
    # response = urllib2.urlopen('http://127.0.0.1:8888/abc')
    url = "https://192.168.1.40:9119/client?uid=client_id&from="
    url = url+fromtime+"&to="
    time=strftime("%Y-%m-%d-%H:%M:%S")
    url=url+time+"&format=yyyy-mm-dd-hh24:mi:ss&token=98a4bafbb35b3527c524ac5d73e9ff8e5e56c6caed488b259682feb7d0a1d192"
    # &from=2014-07-01-23:10:10&to=2014-07-02-23:10:15&format=yyyy-mm-dd-hh24:mi:ss
    # response = urllib2.urlopen('https://192.168.1.40:9119/client?uid=client_id&last=10&token=98a4bafbb35b3527c524ac5d73e9ff8e5e56c6caed488b259682feb7d0a1d192')
    print url
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

    # http = urllib3.PoolManager()
    # r = http.request('GET', 'https://192.168.1.40:9119/client?uid=client_id&last=10&token=98a4bafbb35b3527c524ac5d73e9ff8e5e56c6caed488b259682feb7d0a1d192')
    # htmlsrc_2 = r.data

    # urllib.urlretrieve('https://192.168.1.40:9119/client?uid=client_id&last=10&token=98a4bafbb35b3527c524ac5d73e9ff8e5e56c6caed488b259682feb7d0a1d192')

    json_data=htmlsrc
    print htmlsrc
    data = json.loads(json_data)
    #pprint(data)
    #print "jfl"
    #print json.dumps(data["log entry"], sort_keys=True,indent=4, separators=(',', ': '))
    #print data["log entry"][0]["device_id"]
    #print data["log entry"][1]["client_id"]
    for i in range(0,len(data["log entries"])):
        data["log entries"][i]["date"]=data["log entries"][i].pop("ts")
        data["log entries"][i]["UID"]=data["log entries"][i].pop("device_id")
        data["log entries"][i].pop("client_id")
        data["log entries"][i]["APName"]=data["log entries"][i].pop("label")
        data["log entries"][i].pop("type")
    #print json.dumps(data["log entries"], sort_keys=False,indent=4, separators=(',', ': '))
    #json_data.close()
    keys = ['date', 'UID', 'APName']
    f = open('../buildingwise.csv', 'a')
    dict_writer = csv.DictWriter(f, keys)
    # dict_writer.writer.writerow(keys)
    dict_writer.writerows(data["log entries"])


    #htmlsrc = ""
    #data = r.read(50000)
    #htmlsrc = htmlsrc + data
    #r.release_conn()


    #html = urllib.urlopen('http://127.0.0.1:8888/').read()
    #soup = BeautifulSoup.BeautifulSoup(html)
    #texts = soup.findAll(text=True)
    #visible_texts = filter(visible, texts)
    return render(request, 'demoapp2/index.html',{'htmlsrc': htmlsrc})

def bargraph(request):
    return render(request, 'demoapp2/bar_graph.html')

def buildingwise(request):
    return render(request, 'demoapp2/Building-wise.html')

def peoplewise(request):
    return render(request, 'demoapp2/People-wise.html')

def samplewebsite(request):
    return render(request, 'demoapp2/SampleWebsite.html')

def tabledata(request):
    return render(request, 'demoapp2/table_data.html')
