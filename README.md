# ImageGPSTools

[中文](./README-cn.md)

> ImageGPSTools is a simple and easy-to-use command-line tool for writing GPS coordinates into the EXIF information of photos, which depends on Python3.

## 1. Install dependencies

```shell
pip install requirement.txt
ln -s $(greadlink -f ./imagetools.sh) /usr/local/bin/imagetools
```

## 2. Useage

- Write GPS coordinates by latitude and longitude

  ```shell
  imagetools write_gps ./test.jpg -la 23.542565 -lo 3.926506
  ```

  If the coordinates are in the GCJ02 coordinate system, they can be converted to the WGS84 coordinate system when writing

  ```shell
  imagetools write_gps ./test.jpg -la 23.542565 -lo 3.926506 -g2w
  ```
  
- Write GPS coordinates from a KML file

	```shell
	imagetools write_gps ./test.jpg -k ./test.kml
	```

- Get the GPS coordinates of a photo
  
  ```shell
  imagetools get_gps ./test.jpg
  ```

- Get the map link (supports Google Maps (google) and Amap (gaode))

  ```shell
  imagetools get_gps -o gaode ./test.jpg
  ```