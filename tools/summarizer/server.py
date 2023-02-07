from gensim.summarization import summarize
from flask import Flask, jsonify, request

app: Flask = Flask(__name__)
meta_descr_len_in_words: int = 18


@app.route("/summarize", methods=["POST"])
def respond():
    text: str = request.json["text"]
    summary: str = summarize(text, word_count=meta_descr_len_in_words)

    return jsonify(summary=summary)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8102)
