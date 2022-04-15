import math
import os

import cv2
# PDM
import numpy as np
from flask import Blueprint, Flask, jsonify, request, send_file
from tensorflow.keras.applications import resnet50
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img

bp = Blueprint("routes", __name__)


def make_bitmap(img: np.ndarray):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filter = cv2.getGaussianKernel(31, 11)
    filter = filter * filter.T
    smoothed_im = cv2.filter2D(img, 0, filter)
    _, img = cv2.threshold(smoothed_im, 115, 255, cv2.THRESH_BINARY)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    return img

def get_yt(type: str):
    videos = {
        "matrix": "https://www.youtube.com/embed/0oGJTQCy4cQ",
        "sqrt": "https://www.youtube.com/embed/mbc3_e5lWw0",
        "ineq": "https://www.youtube.com/embed/VgDe_D8ojxw",
        "series": "https://www.youtube.com/embed/_cooC3yG_p0",
        "distribute": "https://www.youtube.com/embed/3NHSwiv_pSE",
        "limit": "https://www.youtube.com/embed/riXcZT2ICjA",
        "integral": "https://www.youtube.com/embed/__Uw1SXPW7s"
    }
    return videos[type]


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


def get_image(filename):
    original = load_img(filename, target_size=(224,224))
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    return image_batch[0]


def predict(file: str):
    im = cv2.imread(file)
    im = make_bitmap(im)
    im = resize_img(im, (224, 224))
    model = load_model("../saved_models/model_hinge.h5")
    types = ['distribute', 'ineq', 'integral', 'limit', 'matrix', 'series', 'sqrt']

    resnet_mse_model = resnet50.ResNet50(weights='imagenet', include_top=False)
    test_img = get_image(file)
    image_batch = np.expand_dims(test_img, axis=0)
    image_batch = np.copy(image_batch)
    image_batch = resnet50.preprocess_input(image_batch)
    feature_input = resnet_mse_model.predict(image_batch)
    predictions = model.predict(feature_input)
    print(predictions)
    pos = np.argmax(predictions)
    pred = types[pos]
    return pred



@bp.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        if f.filename:
            os.makedirs("./uploaded_files", exist_ok=True)
            path = os.path.join("./uploaded_files", f.filename)
            f.save(path)
            math_type = predict(path)
            return get_yt(math_type)

    return "{}"


@bp.route("/favicon.ico")
@bp.route("/static/images/favicon.ico")  # because other apps have the favicon here
def favicon():
    return send_file("./favicon.ico")


@bp.route("/")
def home():
    return send_file("index.html")
