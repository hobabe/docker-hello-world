from flask import Flask

PORT = 8000
MESSAGE = "Hello world! Let do the first version: 1.0.1 \n  [dh-1: feature 1]"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
