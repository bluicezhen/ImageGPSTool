import piexif
from datetime import datetime


def modify_image_gps(file_path: str,
                     file_save_path: str,
                     gps_latitude_ref: str,
                     gps_latitude_degrees: int,
                     gps_latitude_minutes: int,
                     gps_latitude_seconds_100: int,
                     gps_longitude_ref: str,
                     longitude_degrees: int,
                     longitude_minutes: int,
                     longitude_seconds_100: int):
    """Modify image's GPS info. if image's doesn't has GPS info, this function will insert it."""

    exif_dict = piexif.load(file_path)

    exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef] = gps_latitude_ref
    exif_dict['GPS'][piexif.GPSIFD.GPSLatitude] = ((gps_latitude_degrees, 1),
                                                   (gps_latitude_minutes, 1),
                                                   (gps_latitude_seconds_100, 100))
    exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef] = gps_longitude_ref
    exif_dict['GPS'][piexif.GPSIFD.GPSLongitude] = ((longitude_degrees, 1),
                                                    (longitude_minutes, 1),
                                                    (longitude_seconds_100, 100))

    exif_bytes = piexif.dump(exif_dict)

    piexif.insert(exif_bytes, file_path, file_save_path)


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
    create_time_offset_s: str = exif_dict['Exif'][36880].decode('ascii').replace(':', '')

    create_time = datetime.strptime(f'{create_time_s} {create_time_offset_s}', '%Y:%m:%d %H:%M:%S %z')

    return create_time
