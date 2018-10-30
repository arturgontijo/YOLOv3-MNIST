from PIL import Image, ImageOps
import glob
import re


# data/mnist/images/t_50227_c7.png
def enlarge(basewidth=392):
    img_files = glob.glob("data/mnist/images/*.png")
    tam = len(img_files)
    for idx, file_path in enumerate(img_files):
        img = Image.open(file_path)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        out_name = file_path.split(".")[0] + "_{}.png".format(basewidth)
        img.save(out_name, "JPEG")
        print("[{}/{}] {} done!".format(idx, tam, out_name))


def resize_invert(new_size=(64, 64), invert=False):
    img_files = glob.glob("data/mnist/images/*.png")
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


def gen_labels(size=(64, 64)):
    img_files = glob.glob("data/mnist/images/*.png")
    tam = len(img_files)
    for idx, file_path in enumerate(img_files):
        bbox_size = file_path.split("/")[-1]
        bbox_size = bbox_size.split("_")[-1]
        if "c" in bbox_size:
            bbox_size = 28
        else:
            bbox_size = int(bbox_size.split(".")[0])
        x = 0.5
        y = 0.5
        w = bbox_size / size[0]
        h = bbox_size / size[1]
        m = re.search('(\_c)([0-9])', file_path)
        c = m.group(2)
        # <object-class> <x> <y> <width> <height>
        #        c        x   y     w       h
        txt_name = file_path.split("/")[-1]
        txt_name = txt_name.split(".")[0] + ".txt"
        txt_path = "data/mnist/labels/{}".format(txt_name)
        with open(txt_path, "w") as f:
            data = "{} {} {} {} {}".format(c, x, y, w, h)
            f.write(data)
            print("[{}/{}] {} done!".format(idx, tam, txt_path))
