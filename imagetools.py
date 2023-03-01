import argparse
from controllers import write_gps_info_to_img_file, write_gps_info_to_img_file_by_kml, get_gps_from_image_file

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

    # ------- SUB COMMAND for Write GPS information to image file by KML file. -----------------------------------------
    parser_gpxw2g = subparsers.add_parser('write_kml', help='Write GPS information to image file by kml file.')
    parser_gpxw2g.add_argument('image',
                               help='A image file, such as my_photo.jpg')
    parser_gpxw2g.add_argument('-k', '--kml',
                               metavar='',
                               required=True,
                               help='A kml file, like my_travel.kml')
    parser_gpxw2g.set_defaults(func=write_gps_info_to_img_file_by_kml)

    # ------- Get GSP info from image file -----------------------------------------------------------------------------
    parser_ggps = subparsers.add_parser('get_gps', help='Get GSP info from image file')
    parser_ggps.add_argument('image',
                                help='A image file, such as my_photo.jpg')
    parser_ggps.add_argument('-o', '--output',
                                type=str,
                                metavar='',
                                required=False,
                                help='Output format. One of: (google)')
    parser_ggps.set_defaults(func=get_gps_from_image_file)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
