# AUTHOR: Federico G. De Faveri
# DATE:	Aug 2017
# PURPOSE: This python script will get campaign data from Go2Mobi, and make
#          a decision wether to block or not a placement. This is pure 
#					 digital marketing automation.

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
payload = {"start_date": "2017-05-29", "end_date": "2017-05-31", "groupings": ['placement_id'], "columns": ["cost", "revenue"], "filters": [{"field": "campaign_id", "condition": "=", "value": campaign}]}

r = requests.post(url, json=payload, headers=headers)

rhead = r.headers

print rhead

