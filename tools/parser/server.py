from bs4 import BeautifulSoup as soup
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/get_text", methods=["POST"])
def respond():
    html = request.json["html"]
    text: str = soup(html, "html.parser").get_text()
    return jsonify(text=text)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8101)
