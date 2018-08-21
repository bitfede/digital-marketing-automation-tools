#!/usr/local/bin/python

####
# AUTHOR: Federico G. De Faveri
# DATE:	Apr 2018
# PURPOSE: This python script will get live leads data from afflow (monetizer).
#          It will fetch them 5 times in total, one every 15 seconds.
####

import requests
import time
import pprint
import json
import sys

#define pretty print object
pp = pprint.PrettyPrinter(indent=4)

# opening file with credentials
filename = 'tokenfile' 
fincreds=open(filename,'r')

# reading API key off file
key = fincreds.readline()

key = key.rstrip()

# creating base url for our request
base_api_url = "https://api.monetizer.co"

# setting url directory
dir_url = "/data/partner-lead-update.php"

# setting params
# owner = 1
limit = 200

#lead data storage array
lead_data = {}

#number of loops total
total_loops = 20

for x in range(total_loops):

    # setting custom headers
    headers = {
        'Origin': 'https://app.monetizer.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,it-IT;q=0.8,it;q=0.7,ru-RU;q=0.6,ru;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
        'Accept': '*/*',
        'Referer': 'https://app.monetizer.com/',
        'X_AFFLOW_CLIENT_VERSION': 'WEB_0.1.0',
        'Connection': 'keep-alive',
        'X_AFFLOW_API_TOKEN': key,
    }

    # building the url
    url = base_api_url + dir_url
    print("Sending GET request to " + url)
    print("")

    # making the api request
    r = requests.get(url, headers=headers)

    # working with answer
    status = r.status_code

    print("STATUS: " + str(status)) 
    if status != 200:
    	print("Error")

    leadsraw = r.json()
    leads = leadsraw

    for livelead in leads:

        # pp.pprint(leads[0].get('country_code'))
        pp.pprint(livelead)
        print "--------------"

        #get country code
        countrycode = livelead.get('country_code')

        pp.pprint(countrycode)
        print "--------------"        

        # country dict key has already been created
        if countrycode in lead_data:
            #add a point and insert this lead info
            lead_data[countrycode].append(livelead)
        else:
            #create the key to the dict
            lead_data[countrycode] = [livelead]

        #nothing else to do with the individual lead



    print "finished! " + str(x) + "/" + str(total_loops) + "\n"
    time.sleep(15)
    print "resuming!!\n"

for datakey in lead_data:
    # print "examining " + str(datakey)
    sys.stdout.write(datakey + ": ")
    # print "adesso butto " + str(len(lead_data[datakey]))  + " asterischi"
    for onelead in range(len(lead_data[datakey])):
        # print "asterisk yo"
        # pp.pprint(onelead)
        sys.stdout.write("#")
    print " |"

# pp.pprint(lead_data)





