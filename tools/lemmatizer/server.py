import spacy

from flask import Flask, jsonify, request

app = Flask(__name__)

# Load pre-trained models
nlp = {"en": spacy.load("en_core_web_sm"), "ru": spacy.load("ru_core_news_sm")}


def lemmatize(text: str, lang: str) -> list[str]:
    return [token.lemma_ for token in nlp[lang](text)]


@app.route("/respond", methods=["POST"])
def respond():
    text: str = request.json["text"]
    lang: str = request.json["lang"]
    result = lemmatize(text, lang)
    return jsonify(lemmas=result, lang=lang)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8100)
