# AUTHOR: Federico G. De Faveri
# DATE:	Aug 2017
# PURPOSE: This python script will get campaign data from Go2Mobi, and make
#          a decision wether to block or not a placement. This is pure 
#					 digital marketing automation.

import requests
import time

# campaign data

payout = 0.5
campaign = 123456

# reading token into variable

filename = 'tokenfile' 
fin=open(filename,'r')

token = fin.readline()
token = token.rstrip()

#print token #DEBUG

headers = {"Authorization": "Token " + token}