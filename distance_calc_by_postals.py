from math import radians, cos, sin, asin, sqrt
import pandas as pd
import re

colum_names = [
    'country code',
    'postal code',
    'place name',
    'state name',
    'state code',
    'province name',
    'province code',
    'community name',
    'community code',
    'latitude',
    'longitude',
    'accuracy'
]

# LOAD FILE WITH COORDINATES PER POSTAL6 AND POSTAL4 
# DUTCH SYSTEM HAS TWO VARIATIES OF POSTALCODES. POSTAL6 (1234AB) IS STANDARD AND POSTAL4 (1234) ACCUMULATES TO THE 
# SUM OF AREA OF ALL LETTER POSSIBILITIES ASSOCIATED WITH THAT POSTAL4 CODE. POSTAL4 IS THUS LESS PRECISE THEN POSTAL6.
df_postal6_coordinates = pd.read_table('./POSTCODE COORDINATEN DATASETS/NL_full.txt', header = None, names=colum_names)
df_postal4_coordinates = pd.read_table('./POSTCODE COORDINATEN DATASETS/NL.txt', header = None, names=colum_names)
# FILE CAN BE REPLACED BY ANY OTHER DATASET FROM http://download.geonames.org/export/zip/ (other countries untested)

# ---------

# GENERIC CODE FROM THE WEB: Based on the haversine formula
def haversine(lat1, lon1, lat2, lon2):
    
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [float(lon1), float(lat1), float(lon2), float(lat2)])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers
    return c * r

# ----------

# CODE WRITTEN BY kcvanderlinden ON GITHUB (https://github.com/kcvanderlinden/Afstand-tussen-postcodes) #2022-11-22
# WRITTEN FOR USE WITH DUTCH POSTAL CODES
def postal6_to_coordinate(postal6):
    lat = lat_[0] if len(lat_ := df_postal6_coordinates.loc[df_postal6_coordinates['postal code'] == postal6, 'latitude'].values) > 0 else 0
    lon = lon_[0] if len(lon_ := df_postal6_coordinates.loc[df_postal6_coordinates['postal code'] == postal6, 'longitude'].values) > 0 else 0
    return [lat, lon]

def postal4_to_coordinate(postal4):
    lat = lat_[0] if len(lat_ := df_postal4_coordinates.loc[df_postal4_coordinates['postal code'] == postal4, 'latitude'].values) > 0 else 0
    lon = lon_[0] if len(lon_ := df_postal4_coordinates.loc[df_postal4_coordinates['postal code'] == postal4, 'longitude'].values) > 0 else 0
    return [lat, lon]

def distance_between_postals(postal1, postal2):
    lat_lon_postal1 = postal6_to_coordinate(postal1)
    if 0 in lat_lon_postal1: # IF POSTAL6 CODE IS NOT RECOGNIZES, FALL BACK TO POSTAL4 CODE (PROPRIETARY TO DUTCH POSTAL CODE SYSTEM).
        postal1_as4 = re.findall('\d{4}', postal1)
        lat_lon_postal1 = postal4_to_coordinate(postal1_as4[0])
    lat_lon_postal2 = postal6_to_coordinate(postal2)
    if 0 in lat_lon_postal2: # SAME AS FOR postal1 VARIABLE
        postal2_as4 = re.findall('\d{4}', postal2)
        lat_lon_postal2 = postal4_to_coordinate(postal2_as4[0])
    if 0 in lat_lon_postal1 or 0 in lat_lon_postal2: # IF STILL A 0 IS ENCOUNTERED, ALSO POSTAL4 CODE IS NOT RECOGNIZED.
        return 0
    distance = haversine(lat_lon_postal1[0], lat_lon_postal1[1], lat_lon_postal2[0], lat_lon_postal2[1])
    return distance

