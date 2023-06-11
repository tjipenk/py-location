from math import sin, cos, sqrt, atan2, radians

import os
os.environ['USE_PYGEOS'] = '0'
import geopandas as gpd

# Approximate radius of earth in km
R = 6373.0

## geojson file
gjson = "IDN3.json"

peta_kec = gpd.read_file('IDN3.json')
points = peta_kec.copy()

points['geometry'] = peta_kec['geometry'].centroid
points_within = gpd.sjoin(points, peta_kec, how='inner', predicate='within')


print("polygon", peta_kec.head)
print("centroid", points.head)
print("points_within",points_within.head)



lat1 = radians(52.2296756)
lon1 = radians(21.0122287)
lat2 = radians(52.406374)
lon2 = radians(16.9251681)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result: ", distance)
print("Should be: ", 278.546, "km")
