import ntpath
import os

import MapDatumTrans

from tools.dms_dd import dd2dms
from tools.image_gps import modify_image_gps


def write_gps_info_to_img_file(args):
    working_directory = os.getcwd()
    save_directory = f'{working_directory}/output'
    file_name = ntpath.basename(args.image)
    file_full_path = f'{working_directory}/{file_name}'
    file_save_path = f'{save_directory}/{file_name}'

    if not os.path.isdir(save_directory):
        os.mkdir(save_directory)

    if args.wgs84_to_gcj02:
        latitude, longitude = MapDatumTrans.wgs84_to_gcj02(args.latitude, args.longitude)
    elif args.gcj02_to_wgs84:
        latitude, longitude = MapDatumTrans.gcj02_to_wgs84(args.latitude, args.longitude)
    else:
        latitude = args.latitude
        longitude = args.longitude

    print(f'Final location: {latitude}, {longitude}')

    # DD to DMS
    north_or_south, longitude_degrees, longitude_minutes, longitude_seconds, east_or_west, latitude_degrees, \
        latitude_minutes, latitude_seconds = dd2dms(latitude, longitude)

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
