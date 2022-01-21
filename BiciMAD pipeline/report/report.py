#Libraries:

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
from wranglingfolder import wrangling as wr

def centro_buscado():
    bicis_merge1=wr.bicis_merge()
    title = bicis_merge1['Place of Interest'].to_list()
    title2 = np.unique(title)
    centro_buscado = input('Introducir Centro Cultural/Museo:')
    result = process.extractOne(centro_buscado, title2, score_cutoff=90)
    if result is None:
        result = 'No se encuentra ningún Centro Cultural/Museo que coincida'
    return result[0]
