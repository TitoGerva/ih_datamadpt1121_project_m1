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
import acquisitionpy as acq
import analysis as aly


def bicis_merge():
    cultura1=acq.cultura()
    bicimad1=acq.bicimad()
    bicis_merge = pd.merge(cultura1, bicimad1, how ='cross')
    bicis_merge["DISTANCIA"] = bicis_merge.apply(lambda x: aly.distance_meters(x['PUNTO_a'],x['PUNTO_b']), axis = 1)
    return bicis_merge

def bicimad_list():
    bicis_merge1=bicis_merge()
    return bicis_merge1.sort_values(by = "DISTANCIA", ascending = True).groupby('Place of Interest')['tipo_centro','Place address', 'DISTANCIA','BiciMAD Station', 'Station Location', 'dock_bikes'].nth(0).drop(['DISTANCIA'], axis = 'columns')
