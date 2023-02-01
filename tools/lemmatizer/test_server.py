import requests

URL = "http://0.0.0.0:8100/respond"

# Process whole documents
doc_en = (
    "When Sebastian Thrun started working on self-driving cars at "
    "Google in 2007, few people outside of the company took him "
    "seriously."
)

gold_en = [
    "when",
    "sebastian",
    "Thrun",
    "start",
    "work",
    "on",
    "self",
    "-",
    "drive",
    "car",
    "at",
    "Google",
    "in",
    "2007",
    ",",
    "few",
    "people",
    "outside",
    "of",
    "the",
    "company",
    "take",
    "he",
    "seriously",
    ".",
]

doc_ru = (
    "В настоящее время Китай активно продвигает цифровую трансформацию "
    "и интеллектуальное обновление образования."
)

gold_ru = [
    "в",
    "настоящий",
    "время",
    "китай",
    "активно",
    "продвигать",
    "цифровой",
    "трансформация",
    "и",
    "интеллектуальный",
    "обновление",
    "образование",
    ".",
]


if __name__ == "__main__":
    # test lemmatisation in english
    requested_data = {"text": doc_en, "lang": "en"}
    result = requests.post(URL, json=requested_data).json()
    print(result)
    assert result["lemmas"] == gold_en

    # test lemmatisation in russian
    requested_data = {"text": doc_ru, "lang": "ru"}
    result = requests.post(URL, json=requested_data).json()
    print(result)
    assert result["lemmas"] == gold_ru

    print("Success")
