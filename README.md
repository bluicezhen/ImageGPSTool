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

## FAQ

- While viewing the photos using applications like Preview or Adobe Bridge, I noticed that they contain GPS information. However, I encountered an error while trying to perform relevant operations: Error: The file xxx could not obtain valid EXIF data
  Reason: Due to the limited support for GPS information in photos with damaged EXIF information by the piexif library used by this program, it may not be able to read or write the GPS information of photos normally. However, we provide a simple solution: open the directory where the photo is located through Adobe Bridge, then right-click the photo that needs to be fixed, select "Export -> Custom Export" to fix the EXIF information of the photo, so that this program can read and write its GPS information correctly.