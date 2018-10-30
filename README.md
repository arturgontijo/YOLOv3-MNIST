# YOLOv3-MNIST

Train and Test YOLOv3 to detect handwritten digits using MNIST Database.

Clone this Repo:
```
git clone https://github.com/arturgontijo/YOLOv3-MNIST.git
cd YOLOv3-MNIST
pip3 install -r requirements.txt
```

Preparing the MNIST Dataset:
```
python3 utils/prepare_database.py
python3 -c 'import utils.mnist_labels as m; m.enlarge(); m.resize(invert=True); m.gen_labels()'
```

Clone Darknet Repo:
```
git clone https://github.com/pjreddie/darknet.git
```

Compile Darknet (edit Makefile to use GPU, CUDNN and OPENCV).

After you got the `darknet` binary, download the Pretrained Convolutional Weights:

```
wget https://pjreddie.com/media/files/darknet53.conv.74
```

- Train:
```
cd darknet
./darknet detector train ../cfg/mnist.dataset ../cfg/yolov3_mnist.cfg ../darknet53.conv.74
```

- Test:
```
./darknet detector test ../cfg/mnist.dataset ../cfg/yolov3_mnist.cfg ../models/yolov3_mnist.backup IMAGE_PATH -i 0 -thresh 0.5
```