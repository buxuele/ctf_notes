#### Docker basic

1. 下载安装 

   ```bash
   sudo  curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
   ```

2. 检查版本 

   ```bash
   docker version 
   sudo docker run hello-world  
   ```

3. 阿里云镜像加速

   ```bash
   https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors?spm=5176.12901015.0.i12901015.76b5525cM4LvKV
   ```

4.  检查镜像，sudo docker info  在结尾的部分可以看到的．

5. 获取　yolov5 的镜像 

   ```bash
   sudo docker pull ultralytics/yolov5:latest
   ```

6. 运行一个容器 

   ```bash
   sudo docker run --gpus all --ipc=host -it -v "$(pwd)"/coco:/usr/src/coco ultralytics/yolov5:latest
   
   # 不使用 gpu ,使用 cpu 因为的显卡驱动安装还是有问题的.
   sudo docker run  --ipc=host -it -v "$(pwd)"/coco:/usr/src/coco ultralytics/yolov5:latest
   ```

7. 运行自己的命令

   ```bash
   ls .
   ls ../coco
   python train.py
   python test.py
   python detect.py
   ```

8. 