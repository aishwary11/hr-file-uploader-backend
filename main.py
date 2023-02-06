from flask import *

app = Flask(__name__)


@app.route("/file", methods=["POST"])
def main():
    if request.method == "POST":
        f = request.files["file"]
        f.save(f.filename)


if __name__ == "main":
    app.run(debug=True)
