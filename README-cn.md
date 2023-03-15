# ImageGPSTools

> ImageGPSTools是一个简单易用的命令行工具，主要用于向照片的EXIF信息中写入GPS坐标，依赖于Python3。

## 1. 安装

```shell
pip install requirement.txt
ln -s $(readlink -f ./imagetools.sh) /usr/local/bin/imagetools
```

## 2. 使用

- 通过经纬度写入

  ```shell
  imagetools write_gps ./test.jpg -la 23.542565 -lo 3.926506
  ```

  如果坐标是GCJ02坐标系的，可以在写入时转换为WGS84坐标系

  ```shell
  imagetools write_gps ./test.jpg -la 23.542565 -lo 3.926506 -g2w
  ```
  
- 通过KML文件写入

	```shell
	imagetools write_gps ./test.jpg -k ./test.kml
	```

- 获图片经纬度信息

  ```shell
  imagetools get_gps ./test.jpg
  ```

- 获取地图链接（支持 Google Map (google) 和高德地图(gaode)）

  ```shell
  imagetools get_gps -o gaode
  ```

## 常见问题

1. 在使用预览或 Adobe Bridge 等应用程序查看照片时，我发现这些照片带有 GPS 信息。然而，当我执行相关操作时，出现了错误：Error: The file xxx could not obtain valid EXIF data
   原因：由于本程序使用的库 piexif 对于 EXIF 信息受损的照片支持有限，因此可能无法正常读取或写入照片的 GPS 信息。然而，我们提供了一种简单的解决方法：通过 Adobe Bridge 打开照片所在的目录，然后右键点击需要修复的照片，选择“导出 -> 自定义导出”，即可修复该照片的 EXIF 信息，从而使本程序能够正确读写其 GPS 信息。