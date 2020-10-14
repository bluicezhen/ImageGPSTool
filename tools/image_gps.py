import ntpath
import os
from datetime import datetime
from time import strftime

import piexif

from tools.dms_dd import dd2dms


def write_gps_to_image(image_path: str, latitude: float, longitude: float):
    """Modify image's GPS info. if image's doesn't has GPS info, this function will insert it."""
    image_dir_path = os.path.dirname(image_path)
    image_save_dir_path = image_dir_path + '/output'
    image_save_path = ntpath.basename(image_path)

    if not os.path.isdir(image_save_dir_path):
        os.mkdir(image_save_dir_path)

    exif_dict = piexif.load(image_path)
    north_or_south, longitude_degrees, longitude_minutes, longitude_seconds, east_or_west, latitude_degrees, \
        latitude_minutes, latitude_seconds = dd2dms(latitude, longitude)

    exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef] = north_or_south
    exif_dict['GPS'][piexif.GPSIFD.GPSLatitude] = ((latitude_degrees, 1),
                                                   (latitude_minutes, 1),
                                                   (round(latitude_seconds * 100), 100))
    exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef] = east_or_west
    exif_dict['GPS'][piexif.GPSIFD.GPSLongitude] = ((longitude_degrees, 1),
                                                    (longitude_minutes, 1),
                                                    (round(longitude_seconds * 100), 100))

    exif_bytes = piexif.dump(exif_dict)

    piexif.insert(exif_bytes, image_path, image_save_path)


def get_image_create_time(file_path):
    exif_dict = piexif.load(file_path)
    # 0x9003 36867: The date and time when the original image data was generated
    # 0x9004 36868: The date and time when the image was stored as digital data
    # 36867 for use as image create time
    create_time_s: str = exif_dict['Exif'][36867].decode('ascii')

    # 0x9010 36880:	Offset Time
    # 0x9011 36881: Offset Time Original
    # 0x9012 36882: Offset Time Digitized
    # 36880 for use as image create time offset
    try:
        create_time_offset_s: str = exif_dict['Exif'][36880].decode('ascii').replace(':', '')
    except KeyError:
        # Pictures taken by the some camera like Panasonic G85 doesn't write timezone information to image file. In this
        # case, use local timezone.
        create_time_offset_s = strftime("%z")

    create_time = datetime.strptime(f'{create_time_s} {create_time_offset_s}', '%Y:%m:%d %H:%M:%S %z')

    return create_time
