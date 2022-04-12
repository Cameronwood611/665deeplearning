# PDM
from flask import Flask, send_file, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    print(request)
    return "debug"
    if request.method == "POST":
        f = request.files["file"]
        if f.filename:
            f.save(f.filename)
            print(f.read())
        return "file uploaded successfully"
    return "file upload failed"


@app.route("/favicon.ico")
@app.route("/static/images/favicon.ico")  # because other apps have the favicon here
def favicon():
    return send_file("./favicon.ico")


@app.route("/")
def home():
    return send_file("index.html")
