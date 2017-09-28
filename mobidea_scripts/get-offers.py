#!/usr/local/bin/python

####
# AUTHOR: Federico G. De Faveri
# DATE:	Aug 2017
# PURPOSE: This python script will get offers data from Mobidea
####

import requests
import time

# opening file with credentials
filename = 'tokenfile' 
fin=open(filename,'r')

# reading credential keys off file
lgn = fin.readline()
pwd =  fin.readline()

lgn = lgn.rstrip()
pwd = pwd.rstrip()

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
print()

# making the api request
r = requests.get(url, params=payload)

# working with answer
status = r.status_code

print("STATUS: " + str(status)) 
if status != 200:
	print("Error")



#get answer and work with it
rhead = r.headers

print(rhead)
print(r.json())