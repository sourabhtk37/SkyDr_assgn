import glob
import logging
from itertools import groupby

from PIL import Image

from utils import _convert_alt_to_degrees, _convert_to_degress, haversine

log = logging.getLogger(__name__)


def gps_data():
    """
    Loads GPS data from Images and converts it into degrees.
    """
    imagesData = {}

    logging.info("loading images data from JPG files")

    for image in glob.glob('../images/*.JPG'):

        try:
            gps_info = Image.open(image)._getexif()[0x8825]
        except TypeError:
            log.warning("GPSInfo not found")

        gps_latitude_ref = gps_info[1]
        gps_latitude = gps_info[2]
        gps_longitude_ref = gps_info[3]
        gps_longitude = gps_info[4]
        gps_altitude_ref = gps_info[5]
        gps_altitude = gps_info[6]

        lat = _convert_to_degress(gps_latitude)
        if gps_latitude_ref != "N":
            lat = 0 - lat

        lon = _convert_to_degress(gps_longitude)
        if gps_longitude_ref != "E":
            lon = 0 - lon

        alt = _convert_alt_to_degrees(gps_altitude)
        if ord(gps_altitude_ref) != 0:
            alt = 0 - alt

        imagesData[image[10:]] = [lon, lat, alt]

    return imagesData


def srt_data():
    """
    Loads per-frame coordinates from srt file
    """
    
    logging.info("loading coordinates from SRT file")

    with open('../videos/DJI_0301.SRT') as file:
        res = [list(g)
               for b, g in groupby(file, lambda x: bool(x.strip())) if b]

    return res
