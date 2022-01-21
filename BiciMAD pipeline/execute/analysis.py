from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas

def to_mercator(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
    c = gpd.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c

def distance_meters(DISTANCIA_x, DISTANCIA_y):
    # return the distance in metres between to latitude/longitude pair point in degrees (i.e.: 40.392436 / -3.6994487)
    return DISTANCIA_x.distance(DISTANCIA_y)