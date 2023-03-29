import os
from flask import (
    Flask,
    send_file,
    send_from_directory,
)

app = Flask(__name__)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        directory=app.root_path,
        path="favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/")
@app.route("/regimento")
def regimento():
    return send_file(
        os.path.join(app.root_path, "static", "regimento.pdf"),
        mimetype="application/pdf",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", default=8080)))
