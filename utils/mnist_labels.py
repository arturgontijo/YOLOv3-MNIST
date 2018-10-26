from PIL import Image, ImageOps
import glob
import re


def gen_labels(size=(64, 64)):
    img_files = glob.glob("./data/mnist/images/*.png")
    tam = len(img_files)
    for idx, file_path in enumerate(img_files):
        x = 0.5
        y = 0.5
        w = 28 / size[0]
        h = 28 / size[1]
        m = re.search('(\_c)([0-9])', file_path)
        c = m.group(2)
        # <object-class> <x> <y> <width> <height>
        #        c        x   y     w       h
        txt_name = file_path.split("/")[-1]
        txt_name = txt_name.split(".")[0] + ".txt"
        txt_path = "./data/mnist/labels/{}".format(txt_name)
        with open(txt_path, "w") as f:
            data = "{} {} {} {} {}".format(c, x, y, w, h)
            f.write(data)
            print("[{}/{}] {} done!".format(idx, tam, txt_path))


def resize(new_size=(64, 64), invert=False):
    img_files = glob.glob("./data/mnist/images/*.png")
    tam = len(img_files)
    for idx, file_path in enumerate(img_files):
        old_im = Image.open(file_path)
        w, h = old_im.size
        im = Image.new("RGB", new_size)
        im.paste(old_im, (int((new_size[0]-w)/2), int((new_size[1]-h)/2)))
        if invert:
            im = ImageOps.invert(im)
        im.save(file_path, "JPEG")
        print("[{}/{}] {} done!".format(idx, tam, file_path))
