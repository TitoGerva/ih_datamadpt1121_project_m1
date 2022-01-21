import argparse
import sys
import pandas as pd
import numpy as np
import re
import json
import requests
from shapely.geometry import Point
import geopandas as gpd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from analyst import analysis as aly

def bicimad():
    bicimad = pd.read_json('../ddbb/bicimaddb.json')
    bicimad['long_finish'] = [float(i.split(",")[0].replace("[", "")) for i in bicimad["geometry_coordinates"]] #FROM geometry_coordinates to clean and get from the LONGITUDE
    bicimad['lat_finish'] = [float(i.split(",")[1].replace("]", "")) for i in bicimad["geometry_coordinates"]] #FROM geometry_coordinates to clean and get from the LATITUDE
    bicimad = bicimad.drop(['activate', 'light','no_available','reservations_count','geometry_type','geometry_coordinates'], axis=1 ) #Cleaning unuseful columns
    bicimad = bicimad.rename(index=str, columns={'name': 'BiciMAD Station', 'address': 'Station Location'}) # Rename Columns
    bicimad["PUNTO_b"] = bicimad.apply(lambda x: aly.to_mercator(x["lat_finish"],x["long_finish"]), axis = 1)
    return pd.DataFrame(bicimad)

def cultura():
    #APIS from WEBSIDE, transform into DataFrames    
    museos = requests.get('https://datos.madrid.es/egob/catalogo/201132-0-museos.json')
    museos = museos.json()
    museos = pd.json_normalize(museos['@graph'])
    museos = pd.DataFrame(museos)
    centros = requests.get('https://datos.madrid.es/egob/catalogo/200304-0-centros-culturales.json')
    centros = centros.json()
    centros = pd.json_normalize(centros['@graph'])
    centros = pd.DataFrame(centros)
    museos = museos.assign(tipo_centro = "Museos")
    centros = centros.assign(tipo_centro = "Centros Culturales")
    cultura = pd.concat([museos, centros])
    cultura = cultura.drop(['@id', '@type','relation','address.district.@id','address.area.@id','organization.organization-desc','organization.accesibility','organization.schedule','organization.services','organization.organization-name'], axis=1 ) #Cleaning unuseful columns
    cultura = cultura.rename(index=str, columns={'address.locality':'City','address.postal-code':'ZIP Code','title': 'Place of Interest', 'address.street-address': 'Place address','location.latitude': 'lat_started', 'location.longitude': 'long_started'}) # Rename Columns
    cultura = cultura.rename(index=str, columns={"location.latitude": "lat_started", "location.longitude": "long_started"})
    cultura['PUNTO_a'] = cultura.apply(lambda x: aly.to_mercator(x['lat_started'],x['long_started']), axis = 1)
    return pd.DataFrame(cultura)