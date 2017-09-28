####
# AUTHOR: Federico G. De Faveri
# DATE:	Aug 2017
# PURPOSE: This python script will get offers data from Mobidea
####

import requests
import time

# reading token into variable

filename = 'tokenfile' 
fin=open(filename,'r')

token = fin.readline()
token = token.rstrip()

# creating headers, url and payload for our request

headers = {"Authorization": ""}
url = ""
# r = requests.

rhead = r.headers

print rhead