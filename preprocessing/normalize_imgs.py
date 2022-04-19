
import math
import os

import cv2
import numpy as np


def make_bitmap(img: np.ndarray):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filter = cv2.getGaussianKernel(31, 11)
    filter = filter * filter.T
    smoothed_im = cv2.filter2D(img, 0, filter)
    _, img = cv2.threshold(smoothed_im, 115, 255, cv2.THRESH_BINARY)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    return img


def resize_img(im: np.ndarray, dim: tuple):
    y, x = im.shape[0], im.shape[1]
    y_out, x_out = dim

    if y_out > y:
        diff = abs(y_out - y)
        padding = math.ceil(diff / 2)
        im = cv2.copyMakeBorder(im, padding, padding, 0, 0, cv2.BORDER_CONSTANT, None, value=[255, 255, 255])

    if x_out > x:
        diff = abs(y_out - y)
        padding = math.ceil(diff / 2)
        im = cv2.copyMakeBorder(im, 0, 0, padding, padding, cv2.BORDER_CONSTANT, None, value=[255, 255, 255])
    
    im = cv2.resize(im, dim, interpolation= cv2.INTER_CUBIC)
    return im


def display(im):
    cv2.imshow("Image", im)
    cv2.waitKey()
    cv2.destroyAllWindows()



def write_from_dir(read_path: str):
    for file in os.listdir(read_path):
        if os.path.isfile(os.path.join(read_path, file)):
            sub_dir = read_path.split("/")[-1]
            new_dir = "./data/" + sub_dir
            old_filepath = os.path.join(read_path, file)
            new_filepath = os.path.join(new_dir, file)
            os.makedirs(new_dir, exist_ok=True)
            img = cv2.imread(old_filepath)
            if img is not None:
                try:
                    img = resize_img(img, (250, 250))
                except:
                    print(old_filepath)
                cv2.imwrite(new_filepath, img)





dirs = [
    "./Completely_Sorted/FOIL",
    "./Completely_Sorted/Integrals",
    "./Completely_Sorted/Square_Roots",
    "./Completely_Sorted/inequality",
    "./Completely_Sorted/limit",
    "./Completely_Sorted/matrices",
    "./Completely_Sorted/series",
]
for dir in dirs:
    write_from_dir(dir)

