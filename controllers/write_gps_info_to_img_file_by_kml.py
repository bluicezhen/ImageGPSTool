import ntpath
import os

from dateutil.parser import parse as datetime_parse
import xmltodict

from tools.dms_dd import dd2dms
from tools.image_gps import get_image_create_time, modify_image_gps


def write_gps_info_to_img_file_by_kml(args):
    image_create_timestamp = int(get_image_create_time(args.image).timestamp())

    with open(args.kml, 'rb') as f:
        kml_dict: dict = xmltodict.parse(f)
        origin_location_list = kml_dict['kml']['Document']['Folder']['Placemark']['gx:Track']['gx:coord']
        origin_datetime_list = kml_dict['kml']['Document']['Folder']['Placemark']['gx:Track']['when']

        image_location = ''
        i = 0
        for origin_datetime in origin_datetime_list:
            node_timestamp = int(datetime_parse(origin_datetime).timestamp())
            if i == 0:
                if image_create_timestamp < (node_timestamp - 60):
                    print('Error: Image create time dose not match this kml file')
                    exit(1)
            if image_create_timestamp <= node_timestamp:
                image_location = origin_location_list[i]
            i += 1

        if image_location == '':
            print('Error: Image create time dose not match this kml file')
            exit(1)

        image_location_origin = image_location.split(' ')
        longitude = float(image_location_origin[0])
        latitude = float(image_location_origin[1])

        # DD to DMS
        north_or_south, longitude_degrees, longitude_minutes, longitude_seconds, east_or_west, latitude_degrees, \
            latitude_minutes, latitude_seconds = dd2dms(latitude, longitude)

        working_directory = os.getcwd()
        save_directory = f'{working_directory}/output'
        file_name = ntpath.basename(args.image)
        file_full_path = f'{working_directory}/{file_name}'
        file_save_path = f'{save_directory}/{file_name}'
        if not os.path.isdir(save_directory):
            os.mkdir(save_directory)

        # Write GPS information to new image file
        modify_image_gps(
            file_full_path,
            file_save_path,
            north_or_south,
            latitude_degrees,
            latitude_minutes,
            round(latitude_seconds * 100),
            east_or_west,
            longitude_degrees,
            longitude_minutes,
            round(longitude_seconds * 100))