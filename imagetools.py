import argparse
from controllers import write_gps_info_to_img_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='imagetools')
    parser.add_argument('--foo', action='store_true', help='foo help')
    subparsers = parser.add_subparsers(help='sub-command help')

    # ------- SUB COMMAND for Write GPS information to image file. -----------------------------------------------------
    parser_wgpsimg = subparsers.add_parser('write_gps', help='Write GPS information to image file.',
                                           usage='%(prog)s xxx.jpeg [options]')
    parser_wgpsimg.add_argument('image',
                                help='A image file, such as my_photo.jpg')
    parser_wgpsimg.add_argument('-la', '--latitude',
                                type=float,
                                metavar='',
                                required=True,
                                help='Decimal degrees latitude, such as: 22.578829')
    parser_wgpsimg.add_argument('-lo', '--longitude',
                                type=float,
                                metavar='',
                                required=True,
                                help='Decimal degrees longitude, such as: 114.219687')
    parser_wgpsimg.add_argument('-w2g', '--wgs84-to-gcj02',
                                action='store_true',
                                help='Whether convert the GPS info from WGS84 to GCJ02')
    parser_wgpsimg.add_argument('-g2w', '--gcj02-to-wgs84',
                                action='store_true',
                                help='Whether convert the GPS info from GCJ02 to WGS84')
    parser_wgpsimg.set_defaults(func=write_gps_info_to_img_file)

    # ------- SUB COMMAND for Turn WGS84 GPX file to GCJ02 GPX file. ---------------------------------------------------
    parser_gpxw2g = subparsers.add_parser('gpxw2g', help='Turn WGS84 GPX file to GCJ02 GPX file.')
    parser_gpxw2g.add_argument('--baz', choices='XYZ', help='baz help')

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
