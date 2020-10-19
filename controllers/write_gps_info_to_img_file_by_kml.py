from dateutil.parser import parse as datetime_parse
import xmltodict

from tools.image_gps import get_image_create_time, write_gps_to_image


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
                break
            i += 1

        if image_location == '':
            print('Error: Image create time dose not match this kml file')
            exit(1)

        image_location_origin = image_location.split(' ')
        longitude = float(image_location_origin[0])
        latitude = float(image_location_origin[1])

        # Write GPS information to new image file
        write_gps_to_image(args.image, latitude, longitude)
