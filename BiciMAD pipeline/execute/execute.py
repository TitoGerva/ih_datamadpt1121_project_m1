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
import wrangling as wr
import report as ort

parser = argparse.ArgumentParser(description='Get the closest BICIMAD station')
parser.add_argument(
    '--tipo', 
    dest='tipo', 
    default = 'cercana', 
    help = 'Dear User, this app shows the biciMAD station close to the Place of interest selected. Please, Remember the Paremeters to be selected. ENJOY MADRID!. Available Values: cercana , todas'
)
args = parser.parse_args()


if args.tipo == 'cercana':
    test_dataframe = wr.bicis_merge()
    resultado_centro = test_dataframe[test_dataframe['Place of Interest']==ort.centro_buscado()].sort_values(by = "DISTANCIA", ascending = True).head(1)
    resultado_centro.to_csv('ddbb/resultado_BiciMAD_cerca.csv', sep = '|')
    print('File recorded in ddbb folder')
elif args.tipo == 'todas':
    todas = wr.bicimad_list()
    todas.to_csv('ddbb/resultado_BiciMAD_todas.csv', sep= "|")
    print('File recorded in ddbb folder')
else:
    print("WRONG OPTION, Please follow instructions in --help")
