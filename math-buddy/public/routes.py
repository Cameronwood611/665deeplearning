import os

# PDM
from flask import Flask, send_file, request, jsonify

app = Flask(__name__)


@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        if f.filename:
            f.save(os.path.join("./uploaded_files", f.filename))
    return "{}"


# @app.route("/remove", methods=["POST"])
# def remove():
#     if request.method == "POST":
#         f = request.files["file"]
#         if f.filename:
#             os.remove(os.path.join("./uploaded_files", f.filename))
#             return f.filename
#     return ""


@app.route("/favicon.ico")
@app.route("/static/images/favicon.ico")  # because other apps have the favicon here
def favicon():
    return send_file("./favicon.ico")


@app.route("/")
def home():
    return send_file("index.html")
