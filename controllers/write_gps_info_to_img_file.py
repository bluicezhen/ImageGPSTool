import MapDatumTrans

from tools.image_gps import write_gps_to_image


def write_gps_info_to_img_file(args):
    if args.wgs84_to_gcj02:
        latitude, longitude = MapDatumTrans.wgs84_to_gcj02(args.latitude, args.longitude)
    elif args.gcj02_to_wgs84:
        latitude, longitude = MapDatumTrans.gcj02_to_wgs84(args.latitude, args.longitude)
    else:
        latitude = args.latitude
        longitude = args.longitude

    print(f'Final location: {latitude}, {longitude}')

    # Write GPS information to new image file
    write_gps_to_image(args.image, latitude, longitude)
