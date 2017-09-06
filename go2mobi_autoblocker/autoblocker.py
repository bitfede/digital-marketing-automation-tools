####
# AUTHOR: Federico G. De Faveri
# DATE:	Aug 2017
# PURPOSE: This python script will get campaign data from Go2Mobi, and make
#          a decision wether to block or not a placement. This is pure 
#					 digital marketing automation.
####

import requests
import time

# campaign data

payout = 0.5
campaign = 203649

# reading token into variable

filename = 'tokenfile' 
fin=open(filename,'r')

token = fin.readline()
token = token.rstrip()

# creating headers, url and payload for our request

headers = {"Authorization": "Token " + token}
url = "https://api.go2mobi.com/v1/reports"
payload = {"start_date": "2017-01-01", "end_date": "2017-08-01", "groupings": ['placement_id'], "columns": ["cost", "revenue"], "filters": [{"field": "campaign_id", "condition": "=", "value": campaign}]}

r = requests.post(url, json=payload, headers=headers)

rhead = r.headers

print rhead

status = ""

while status != "200 OK":
	payload2 = {"page_size": 300, "page_number": 1}
	r2 = requests.get(rhead["Location"], params = payload2, headers=headers)
	status = r2.headers["Status"]
	print "working ... status: " + status
	time.sleep(5)


req2json = r2.json()

print "--RESPONSE--"
print req2json

for line in req2json["records"]:
	print line["placement_id"]
	if float(line["cost"]) > payout*2 and float(line["revenue"]) < payout:
		print line["placement_id"] + " is a bad placement " + line["cost"]
		payload3 = {"type": "block", "placement_id": line["placement_id"]}
		url3 = "https://api.go2mobi.com/v1/campaigns/" + str(campaign) + "/rules/"
		r3 = requests.post(url3, params=payload3, headers=headers)
		print "blacklisting was ... " + r3.headers()









