#!/usr/bin/python

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

print("STATUS: " + str(status)) 
if status != 200:
	print("Error!!!! <<<<<<<<")

#receive the login api token
login_api_token = r.json()["api_token"]

#setting variables
url2 = base_api_url + '/campaigns'
bearer_token = "Bearer " + login_api_token
header2 = { "Authorization": bearer_token }
payload2 = { "status[]": "6", "is_archived": "0"}

# make the get all campaigns request
r2 = requests.get(url2, headers=header2, params=payload2)

#get the r2 status
status2 = r2.status_code

print ('R2 STATUS ----')
print status2

pp.pprint(r2.json())




