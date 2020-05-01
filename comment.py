
import httplib, urllib
from bs4 import BeautifulSoup
import os
import json
import time

access_token= raw_input("Enter Your Token:")
stsid = raw_input("Enter Your Target Status ID:")
url = "/"+raw_input("Enter Your Target sts ID")
msg = raw_input("Enter Message!:")
conn = httplib.HTTPSConnection("graph.facebook.com")
print 'Please Wait!'

def comment(url):
    connect = httplib.HTTPSConnection("graph.facebook.com")
    connect.request("GET",url)
    for x in xrange(1000):

            print 'commenting %d '% x
            path ='/'+stsid+'/comments'
            param_data={  'format':'json',
                        'message':msg,
                        'access_token':access_token
                  }
            connect = httplib.HTTPSConnection("graph.facebook.com")
            connect.request("POST",path,urllib.urlencode(param_data),                  >
            time.sleep(10.09)


comment(url)
print 'DONE!'
