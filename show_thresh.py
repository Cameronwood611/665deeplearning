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


img = cv2.imread("./sample_imgs/mat.png")
img = make_bitmap(img)
cv2.imshow ("grayscale", img)
cv2.waitKey()
cv2.destroyAllWindows()
