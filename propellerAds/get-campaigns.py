#!/usr/local/bin/python

####
# AUTHOR: Federico G. De Faveri
# DATE:	Apr 2018
# PURPOSE: This python script will get campaigns data from propellerads
####

import requests
import time
import pprint

#define pretty print object
pp = pprint.PrettyPrinter(indent=4)

# opening file with credentials
filename = 'tokenfile' 
fincreds=open(filename,'r')

# reading API key off file
key = fincreds.readline()

key = key.rstrip()

# creating base url for our request
base_api_url = "http://report.propellerads.com"

# setting params
action = 'getStats'
date_range = 'last_7_days'
stat_columns = ['show','click','convers','convrate','cpm','ctr','profit']
group_by = 'campaign_id'

# setting payload
payload = { 'action': action, 'key': key , 'date_range': date_range , 'stat_columns': stat_columns , 'group_by': group_by}

# building the url
url = base_api_url
print("Sending GET request to " + url)
print("")

# making the api request
r = requests.get(url, params=payload)

# working with answer
status = r.status_code

print("STATUS: " + str(status)) 
if status != 200:
	print("Error")









