import urllib,urllib2,urllib3
import BeautifulSoup
import json,csv
from django.shortcuts import render
from django.http import HttpResponseRedirect
from newapp.models import *
from time import strftime
from datetime import *
htmlsrc=""
time="2015-07-03-17:20:10"
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

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
	response = urllib2.urlopen(url)
	htmlsrc = response.read()
	
	# http = urllib3.PoolManager()
	# r = http.request('GET', 'https://192.168.1.40:9119/client?uid=client_id&last=10&token=98a4bafbb35b3527c524ac5d73e9ff8e5e56c6caed488b259682feb7d0a1d192')
	# htmlsrc_2 = r.data

	# urllib.urlretrieve('https://192.168.1.40:9119/client?uid=client_id&last=10&token=98a4bafbb35b3527c524ac5d73e9ff8e5e56c6caed488b259682feb7d0a1d192')
	
	json_data=htmlsrc

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
