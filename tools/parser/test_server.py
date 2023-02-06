import requests

URL = "http://0.0.0.0:8101/get_text"

# Process whole documents
html = (
    "In addition, there is information about the Insight Report on ICT in Higher"
    " Education and TVET in the Middle East and Pakistan <a href="
    "'https://iite.unesco.org/news/ict-in-he-and-tvet-in-middle-east-and-pakistan/'"
    ">“Talent Ecosystem for Digital Transformation”</a>, published by UNESCO IITE."
)

golden = (
    "In addition, there is information about the Insight Report"
    " on ICT in Higher Education and TVET in the Middle East and"
    " Pakistan “Talent Ecosystem for Digital Transformation”,"
    " published by UNESCO IITE."
)

if __name__ == "__main__":
    # test lemmatisation in english
    result: dict[str, str] = requests.post(URL, json={"html": html}).json()
    print(result["text"])
    assert result["text"] == golden
    print("Success")
