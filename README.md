# YOLOv3-MNIST

Train and Test YOLOv3 to detect handwritten digits using MNIST Database.

- Train:
```
./darknet/darknet detector train cfg/mnist.dataset cfg/yolov3_mnist.cfg darknet53.conv.74
```

- Test:
```
./darknet/darknet detect cfg/yolov3_mnist.cfg models/yolov3_mnist.backup IMAGE_PATH
```