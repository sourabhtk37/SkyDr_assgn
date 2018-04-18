import logging
from math import asin, cos, radians, sin, sqrt

log = logging.getLogger(__name__)


# todo: altitude/elevation is added but needs to be checked for accuracy
def haversine(lon1, lat1, lon2, lat2, alt1=0, alt2=0):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    mean_earth_radius = 6371   # in Km

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, list(
        map(float, [lon1, lat1, lon2, lat2])))

    # haversine formula with altitude
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    dalt = alt2 - alt1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    distance = mean_earth_radius * c * 1000  # to meters

    distance = distance ** 2 + dalt ** 2

    return sqrt(distance)


def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored in 
    the EXIF to degress in float format
    """

    degrees = float(value[0][0]) / float(value[0][1])

    minutes = float(value[1][0]) / float(value[1][1])

    seconds = float(value[2][0]) / float(value[2][1])

    return degrees + (minutes / 60.0) + (seconds / 3600.0)


def _convert_alt_to_degrees(value):
    """
    Helper function to convert the GPSAltitude stored in 
    the EXIF to degress in float format
    """

    return float(value[0]) / float(value[1])
