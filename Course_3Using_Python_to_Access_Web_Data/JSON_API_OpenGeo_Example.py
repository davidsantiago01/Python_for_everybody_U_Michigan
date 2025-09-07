import urllib.request, urllib.parse
import http, json, ssl

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'


while True:
    address = input ("Enter Location")
    if len (address) <1 :break

    address = address.strip()
    parms = dict()
    parms ["q"] = address

    url = serviceurl + urllib.parse.urlencode (parms)

    print ("Retrieving", url)
    uh = urllib.request.urlopen (url, context = ctx)
    data = uh.read().decode()
    print ("Retrieved", len(data), "characters", data[:20].replace("\n", " "))

    js = json.loads (data)
    
    lat = js['features'][0]["properties"]["lat"]
    lon = js['features'][0]["properties"]["lon"]
    print ("lat", lat, "lon", lon)
    location = js['features'][0]["properties"]["formatted"]
    print (location)
  
Retrieving http://py4e-data.dr-chuck.net/opengeo?q=Ann+Arbor%2C+MI
Retrieved 1339 characters {"type":"FeatureColl
lat 42.2813722 lon -83.7484616
Ann Arbor, MI, United States of America

#Service Oriented Architecture - allows an application to be broken into parts and distrubuted accross a network
#An application (API) program interface is a contract for interaction
#Web Services provide infrastructure for applications cooperating (an API) over a network - a SOAP  and REST are two styles of web services
#XML and JSON are serialisation formats
