import os
os.environ['USE_PYGEOS'] = '0'
import geopandas as gpd
import pandas as pd

## geojson file
peta_kec = gpd.read_file('IDN3.json')
# point_kec = peta_kec.copy()
# point_kec['geometry'] = peta_kec['geometry'].centroid

def geo_lokasi(lat_src, lon_src, lat_dst, lon_dst, peta_kec=peta_kec):
    ## source lat lon -6.2515958, 106.8415269
    # lat_src = -6.2515958
    # lon_src = 106.8415269

    ## destination lat lon -6.562744, 106.726071
    # lat_dst = -6.562744
    # lon_dst = 106.726071

    # lokasi = gpd.points_from_xy(lon,lat, crs="EPSG:4326") ## WGS84
    lokasi = pd.DataFrame(
        {
            "keterangan" : ['src','dst'],
            "lat" : [lat_src, lat_dst],
            "lon" : [lon_src, lon_dst],
        }
    )

    lokasi_4326 = gpd.GeoDataFrame(
        lokasi, geometry=gpd.points_from_xy(lokasi.lon, lokasi.lat), crs="EPSG:4326"
    )
    ## EPSG:3857 WGS 84 / Pseudo-Mercator -- Spherical Mercator, Google Maps, OpenStreetMap, Bing, ArcGIS, ESRI
    lokasi_utm = lokasi_4326.to_crs('EPSG:3857')

    point_src = lokasi_utm
    point_dst = point_src.shift() 

    jarak = point_src.distance(point_dst)[1]/1000
    print("Jarak :", round(jarak,2) ," km")

    points_within = gpd.sjoin(lokasi_4326, peta_kec, how='inner', predicate='within')
    info_src = points_within
    info_dst = points_within
    print("Lokasi Asal :",info_src.NAME_1[0], info_src.NAME_2[0], info_src.NAME_3[0] )
    print("Lokasi Tujuan :",info_src.NAME_1[1], info_src.NAME_2[1], info_src.NAME_3[1] )
    result = {
        "jarak_km" : round(jarak,2),
        "lokasi_asal" : info_src.NAME_1[0] + ', ' + info_src.NAME_2[0] + ", " + info_src.NAME_3[0],
        "lokasi_tujuan" : info_src.NAME_1[1] + ', ' + info_src.NAME_2[1] + ", " + info_src.NAME_3[1]
    }
    return result

