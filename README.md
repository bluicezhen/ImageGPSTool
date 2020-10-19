# ImageGPSTools

[中文](./README-cn.md)

> ImageGPSTools is a simple command line tool for write GPS information to image's EXIF which depended Python3.

## 1. Install

> The sample is for reference only. It's worked on MacOS 10.15.7

## 2. Install dependencies

```shell
pip install requirement.txt
ln -s $(greadlink -f ./imagetools.sh) /usr/local/bin/imagetools
```

## 3. Useage

- By longitude and latitude

  ```shell
  imagetools write_gps ./test.jpg -la 23.542565 -lo 3.926506
  ```

  If GCJ02, we can tranlate to WSG84.

  ```shell
  imagetools write_gps ./test.jpg -la 23.542565 -lo 3.926506 -g2w
  ```
  
- By KML file

	```shell
	imagetools write_gps ./test.jpg -k ./test.kml
	```