#!/usr/bin/python

####
# AUTHOR: Federico G. De Faveri
# DATE:	Apr 2018
# PURPOSE: This python script will get campaigns data from propellerads
####

import requests
import time
import datetime
import pprint
import json

#define payout value
PAYOUT = 0.56

#define pretty print object
pp = pprint.PrettyPrinter(indent=4)

# opening file with credentials
filename = 'tokenfile' 
fincreds=open(filename,'r')

# reading API key off file
key = fincreds.readline()

key = key.rstrip()

# creating base url for our request
base_api_url = "https://ssp-api.propellerads.com/v5/adv"

# setting params
password = key.split(" ")[0]
username = key.split(" ")[1]

# setting payload
payload = { 'username': username, 'password': password }

# building the url
url = base_api_url + '/login'
print("Sending GET request to " + url)
print("")

# making the api request
r = requests.post(url, params=payload)

# working with answer
status = r.status_code

print("r1 STATUS: " + str(status)) 
if status != 200:
	print("Error!!!! <<<<<<<<")
	exit(1)

#receive the login api token
login_api_token = r.json()["api_token"]

#setting variables
url2 = base_api_url + '/campaigns'
bearer_token = "Bearer " + login_api_token
header2 = { "Authorization": bearer_token, 'Content-Type': 'application/json'}
payload2 = { "status[]": "6", "is_archived": "0"}

# make the get all campaigns request
r2 = requests.get(url2, headers=header2, params=payload2)

#get the r2 status
status2 = r2.status_code

print ('r2 STATUS: ' + str(status2))

if status2 != 200:
	print("Error!!!! <<<<<<<<")
	exit(2)

#get all the running campaigns
r2_results = r2.json()["result"]

#create a camp id array and get ids
running_camps_id = []

for r2_result in r2_results:
	running_camps_id.append(r2_result["id"])

for camp_id in running_camps_id:

	##get the zones
	print("--- Optimizing Camp " + str(camp_id))
	#variables
	url3 = base_api_url + '/statistics/zones'
	today = datetime.datetime.today().strftime('%Y-%m-%d')
	payload3 = {"campaign_id[]": [camp_id] , "date_from": "2018-01-01", "date_to": today }
	
	r3 = requests.get(url3, headers=header2, params=payload3)

	status3 = r3.status_code
	print "r3 STATUS: " + str(status3)

	if status3 != 200:
		print("Error!!!! <<<<<<<<")
		exit(3)

	r3_result = r3.json()["result"]

	# create temp list of blacklisted zones
	zone_blacklist = []
	counter = 0
	countertot = 0

	# loop thru zones

	for zone in r3_result:
		countertot += 1
		zone_spent = float(zone["money"])
		if (zone["conversions"] > '0'):
			if (float(zone["money"]) > PAYOUT*2):
				print "########################"
				print "ZONE#" + zone["zone_id"]
				print "spent: " + zone["money"]
				print "Added to BLOCK list"
				print "########################"
				zone_blacklist.append(str(zone["zone_id"]))
				counter = counter + 1
		else:
			#no conversion zones, just check if they spent too much
			if (zone["conversions"] == '0'):
				if (float(zone["money"]) > PAYOUT):
					print "########################"
					print "ZONE#" + zone["zone_id"]
					print "spent: " + zone["money"]
					print "BLOCKED---"
					print "########################"
					zone_blacklist.append(str(zone["zone_id"]))
					counter = counter + 1

	print "I will block " + str(counter) + " zones! out of " + str(countertot) + " || for camp: " + str(camp_id)  

	# create request to block zones for current camp ~!!
  #TODO !!!
	url4 = base_api_url + '/campaigns/' + str(camp_id) + '/targeting/exclude/zone'
	payload4 = json.dumps({"zone": zone_blacklist})

	r4 = requests.put( url4 , data=payload4,  headers=header2)

	status4 = r4.status_code
	print "r4 STATUS: " + str(status4)
	print header2
	print "----"
	print (r4.json())

	if status4 != 200:
		print("Error!!!! <<<<<<<<")
		exit(3)










