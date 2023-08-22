from flask import Flask
from src import utils

app = Flask(__name__)


@app.route("/")
def index():
    message = {
        "message": "Hello world",
        "version": "1.0.0"
    }
    return utils.json_response(message)


if __name__ == "__main__":
    app.run()
