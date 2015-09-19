import math
from geopy.geocoders import Nominatim

geolocator = Nominatim()

def is_in_circle(circle_x, circle_y, r, x, y):
    d = math.sqrt((circle_x - x)**2 + (circle_y - y)**2)
    if d <= r:
        print "within!"
    else:
        print "not within"

location1 = geolocator.geocode("Toronto")
location2 = geolocator.geocode("Art Gallery of Ontario")

range = 5.0
radius = range/68.703

#print(location.address)
#Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
#print((location.latitude, location.longitude))
#(40.7410861, -73.9896297241625)
is_in_circle(location1.latitude, location1.longitude, radius, location2.latitude, location2.longitude)