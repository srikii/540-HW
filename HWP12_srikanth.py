"""python program to calculate the distance between the whitehouse and given location in miles
    author: srikanth """
import urllib.request
import urllib.parse
import urllib.error
import json

import ssl
from math import sin, cos, sqrt, asin, radians

serviceurl = "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?"

while True:

    url_whitehouse = 'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=1600+Pennsylvania+Avenue%2C+Washington%2C+DC&benchmark=Public_AR_Current&format=json'
    uh = urllib.request.urlopen(url_whitehouse)
    data = uh.read().decode()

    x = "&benchmark=Public_AR_Current&format=json"
    address = input('Enter location: ')
    if len(address) < 1:
        break
    url = serviceurl + urllib.parse.urlencode({'address': address})
    #url='https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=74+reservoir+avenue,+jersey+city,+new+jersey&benchmark=Public_AR_Current&format=json'
    print('Retrieving', url+x)
    uh2 = urllib.request.urlopen(url+x)
    data2 = uh2.read().decode()

    print('Retrieved', len(data2), 'characters')

    try:
        js = json.loads(data)
        js2 = json.loads(data2)
    except:
        js = None
        js2 = None

    lat = js["result"]["addressMatches"][0]["coordinates"]["x"]
    lng = js["result"]["addressMatches"][0]["coordinates"]["y"]

    try:
        lat2 = js2["result"]["addressMatches"][0]["coordinates"]["x"]
        lng2 = js2["result"]["addressMatches"][0]["coordinates"]["y"]
    except IndexError:
        print("invalid address ")
        continue

    print("coordinates of the given address is",
          '\nlat: ', lat2, '\nlng: ', lng2)

    lng, lat, lng2, lat2 = map(radians, [lng, lat, lng2, lat2])
    R = 3956
    dlon = lng2 - lng
    dlat = lat2 - lat
    a = sin(dlat/2)**2 + cos(lat) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(min(1, sqrt(a)))
    d = R * c

    print("distance between The white house and your address is: ", d, " miles")

    ret = input("press R to restart")
    if ret.upper() == "R":
        continue
    else:
        exit()
