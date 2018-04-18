import csv
import logging.config

from calc_drone_path import trace_drone_path
from load_data import gps_data, srt_data
from utils import haversine

logging.config.fileConfig('../logging.conf')
log = logging.getLogger(__name__)


def write_to_file(frame_number, image_list):
    """
    Perform write operation per frame
    """
    with open('spreadsheets/video_srt_image_data.csv', 'a') as outfile:
        outfile.write(frame_number.replace(',', '.'))
        outfile.write(',')
        outfile.write(':'.join(image_list))
        outfile.write('\n')


def get_images(images_data, lon2, lat2, radius):
    """
    Retrieves images lying within the radius of a 
    frame location using haversine formulae.
    """

    image_list = []

    for image_name, image_data in images_data.items():
        lon1, lat1, alt1 = map(float, image_data)

        distance = haversine(lon1, lat1, lon2, lat2)

        if distance < radius:
            image_list.append(image_name)

    return image_list


def check_frames(frames, images_data):
    """
    Retreive images 35m near to a particular frame 
    and writes it csv.
    """
    for frame in frames:
        lon2, lat2, alt2 = frame[2].strip('\n').split(',')
        image_list = get_images(images_data, lon2, lat2, 35)
        write_to_file(frame[1].split('-->')[0], image_list)


def check_poi(filename, images_data):
    """
    Adds all images lying 50m near to Point of interests. 
    """

    with open(filename, 'r') as rfile, open('spreadsheets/asset_poi.csv', 'w') as wfile:

        reader = csv.DictReader(rfile)

        fieldnames = ['asset_name', 'longitude', 'latitude', 'image_names']
        writer = csv.DictWriter(wfile, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:
            lon2 = row['longitude']
            lat2 = row['latitude']
            image_list = get_images(images_data, lon2, lat2, 50)

            row['image_names'] = ':'.join(image_list)
            writer.writerow(row)


def main():
    """
    Driver function
    """
    images_data = gps_data()
    frames = srt_data()

    check_frames(frames, images_data)
    check_poi('../assets.csv', images_data)

    trace_drone_path(frames)


if __name__ == '__main__':
    main()
