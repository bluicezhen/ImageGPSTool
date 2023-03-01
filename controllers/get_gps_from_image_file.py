from tools.image_gps import get_gps_from_image
from tools.dms_dd import dms2dd

def get_gps_from_image_file(args):
    lat_dms, lat_ref, lon_dms, lon_ref = get_gps_from_image(args.image)
    lat, lon = dms2dd(lat_dms, lat_ref, lon_dms, lon_ref)

    if args.output:
        if args.output == 'google':
            print(f'https://www.google.com/maps/search/?api=1&query={lat}%2c{lon}')
            return
        else:
            print(f'Error: Unknow output format')

    print(f'dd: {lat},{lon}')
    print(f'dms: {lat_dms[0]}°{lat_dms[1]}\'{lat_dms[2]}"{lat_ref} {lon_dms[0]}°{lon_dms[1]}\'{lon_dms[2]}"{lon_ref}')