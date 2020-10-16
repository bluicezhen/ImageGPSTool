# ImageGPSTools

> ImageGPSTools是一个简单易用的命令行工具，主要用于向照片的EXIF信息中写入GPS坐标，依赖于Python3。

## 1. 安装

> 在`MacOS 10.15.7`测试通过，其他系统请自己想办法。

```shell
pip install requirement.txt
ln -s $(greadlink -f ./imagetools.sh) /usr/local/bin/imagetools
```

## 2. 使用

- 通过经纬度写入文件

  ```shell
  imagetools write_gps test.jpg -la 23.542565 -lo 3.926506
  ```

  如果坐标是GCJ02坐标系的，可以在写入时转换为WGS84坐标系

  ```shell
  imagetools write_gps test.jpg -la 23.542565 -lo 3.926506 -g2w
  ```

  ​	

