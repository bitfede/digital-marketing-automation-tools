#!/usr/local/bin/python

####
# AUTHOR: Federico G. De Faveri
# DATE:	Aug 2017
# PURPOSE: This python script will get offers data from Mobidea
####

import requests
import time
import pprint

#define pretty print object
pp = pprint.PrettyPrinter(indent=4)

# opening file with credentials
filename = 'tokenfile' 
fincreds=open(filename,'r')

# opening file with offers
filename = 'offerlist.txt' 
finoffers=open(filename,'r')

# reading credential keys off file
lgn = fincreds.readline()
pwd =  fincreds.readline()

lgn = lgn.rstrip()
pwd = pwd.rstrip()

# reading offer numbers off file and storing them into an array
offersArr = []
for lineoffer in finoffers:
	offersArr.append(lineoffer.rstrip())

# creating base url for our request
base_api_url = "https://affiliates.mobidea.com/api/export"

# listing api endpoints
endpoints = dict([('offers', '/offers')])

# setting params
currencies = dict([('euro', 'EUR'), ('dollar', 'USD') ])

# setting payload
payload = { 'login': lgn , 'password': pwd , 'currency': currencies['euro'] , 'format': 'json'}

# building the url
url = base_api_url + endpoints['offers']
print("Sending GET request to " + url)
print("")

# making the api request
r = requests.get(url, params=payload)

# working with answer
status = r.status_code

print("STATUS: " + str(status)) 
if status != 200:
	print("Error")



#get answer and work with it
rhead = r.headers

r_json = r.json()

# testing shit
pp.pprint(r_json[1])

print "------"
# offerinfo = r_json[1][0]["_value"]
# offernumber = offerinfo.split("-") 
# print offernumber[0]

# loop
for i in r_json:
	offerinfo = i[0]["_value"]
	offernumber = offerinfo.split("-")
	offernumber = str(offernumber[0].strip())
	if offernumber in offersArr:
		print offernumber
 

















