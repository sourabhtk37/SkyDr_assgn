import csv
import logging

import simplekml

log = logging.getLogger(__name__)
kml = simplekml.Kml()


def trace_drone_path(frames):
    logging.info("Creating drone path")
    lineString = kml.newlinestring(name="Drone path")

    for frame in frames:
        longitude, latitude, altitude = frame[2].strip('\n').split(',')
        lineString.coords.addcoordinates([(longitude, latitude, altitude)])
    
    try:
        kml.save('kml_paths/drone_path.kml')
    except IOError:
        logging.error("Drone path was not created")
