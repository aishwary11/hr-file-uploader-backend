from flask import *

app = Flask(__name__)


@app.route("/file", methods=["POST"])
def main():
    if request.method == "POST":
        f = request.files["file"]
        d = request.files["description"]
        f.save(f.filename)
        d.save(d)


if __name__ == "main":
    app.run(port=5000, debug=True)
