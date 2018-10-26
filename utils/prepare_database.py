import numpy as np
import cv2
import os


def conv_mnist(img_file, label_file, num, path, list_file, label):

    imgs = open(img_file, "rb").read()
    imgs = np.fromstring(imgs, dtype=np.uint8)
    imgs = imgs[16:]
    imgs = imgs.reshape((num, 28, 28))

    labels = open(label_file,"rb").read()
    labels = np.fromstring(labels, dtype=np.uint8)
    labels = labels[8:]

    fw = open(list_file, "w")
    for i in range(num):
        class_id = labels[i]
        img_name = "%s_%05d_c%d.png" % (label, i, class_id)
        img_path = path + "/" + img_name
        cv2.imwrite(img_path, imgs[i])
        fw.write(img_path + "\n")
    fw.close()


cwd = os.getcwd()

mnist_folder = cwd + "/data/mnist"
images_path = cwd + "/data/mnist/images"
labels_path = cwd + "/data/mnist/labels"

if not os.path.exists(images_path):
    if not os.path.exists(mnist_folder):
        os.mkdir(mnist_folder)
    os.mkdir(images_path)
    os.mkdir(labels_path)

t = [cwd + "/data/" + "t10k-images-idx3-ubyte",
     cwd + "/data/" + "t10k-labels-idx1-ubyte",
     cwd + "/data/" + "train-images-idx3-ubyte",
     cwd + "/data/" + "train-labels-idx1-ubyte"]

data_files = ["train-images-idx3-ubyte.gz",
              "train-labels-idx1-ubyte.gz",
              "t10k-images-idx3-ubyte.gz",
              "t10k-labels-idx1-ubyte.gz"]

for data_file in data_files:
    data_path = cwd + "/data/" + data_file
    if not os.path.exists(data_path):
        os.system('curl -O http://yann.lecun.com/exdb/mnist/{}'.format(data_file))
        os.system('gunzip ' + data_file)

for file in t:
    curr_file = file.split("/")[-1]
    os.rename(curr_file, file)

conv_mnist(t[0], t[1], 10000, images_path, "data/mnist/mnist.valid.list", "v")
conv_mnist(t[2], t[3], 60000, images_path, "data/mnist/mnist.train.list", "t")