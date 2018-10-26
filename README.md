# YOLOv3-MNIST

Train and Test YOLOv3 to detect handwritten digits using MNIST Database.

Clone this Repo:
```
git clone https://github.com/arturgontijo/YOLOv3-MNIST.git
cd YOLOv3-MNIST
```

Clone Darknet Repo:
```
git clone https://github.com/pjreddie/darknet.git
```

Compile Darknet (edit Makefile to use GPU, CUDNN and OPENCV).

After you got the `darknet` binary:

- Train:
```
./darknet/darknet detector train cfg/mnist.dataset cfg/yolov3_mnist.cfg darknet53.conv.74
```

- Test:
```
./darknet/darknet detect cfg/yolov3_mnist.cfg models/yolov3_mnist.backup IMAGE_PATH
```