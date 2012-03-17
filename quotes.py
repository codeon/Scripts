import urllib
import json

accesstoken="" # from graph api explorer
y=urllib.urlopen(url)
z=y.read()
data=json.loads(z)
quotes=[]
for i in data['data']:
	urlnew="https://graph.facebook.com/"+str(i['id'])+"?fields=quotes&access_token=AAACEdEose0cBAPHJdsNkrMmWBZAOk93yS3thIVKSWB6ZCZB3C2rR4DK3cOLko7mC9HYp5NGZBB9cDxYUKjMQmAsuQ7X0DYLqKGR4VeceMgZDZD"
	aa=urllib.urlopen(urlnew)
	try:
		ada=json.loads(aa.read().encode('ascii', 'ignore'))
		if "quotes" in ada:
			try:
				print ada['quotes']
				quotes.extend(ada['quotes'])
			except:
				print 
	except:
		print 
	
