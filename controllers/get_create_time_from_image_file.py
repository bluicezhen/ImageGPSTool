from tools.image_gps import get_create_time_from_image

def get_create_time_from_image_file(args):
    ct = get_create_time_from_image(args.image)

    if args.output == 'touch':
        t = ct.replace(':', '').replace(' ', '')
        print(t[:-2] + '.' + t[-2:])
        return

    print(ct)