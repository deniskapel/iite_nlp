import requests

URL = "http://0.0.0.0:8102/summarize"

text = (
    "Dance4Life Belarus launching a new stage of Champion4Life training."
    "Since 2020, the Belarusian Association of UNESCO Clubs has started"
    " implementing the Dance4Life program in Belarus. This project aims to"
    " enhance leadership qualities in young people, promote a healthy lifestyle"
    ", and prevent HIV infection and drug use among youth."
    " In the autumn of 2022, the Belarusian Association of UNESCO Clubs launched"
    " the second stage of the Dance4Life Belarus project (“Journey4Life”) and"
    " conducted training to prepare a new generation of Champions4Life."
    " Champions are the young people who volunteer as facilitators to lead"
    " the modules within the project. As a result of the training, twenty-four"
    " participants from Brest, Gomel, Grodno, Mogilev, Molodechno, Minsk,"
    " Rogachev, and Slutsk received the Champion4Life status."
    " The training course began with an introductory seminar, where officials"
    " and program coordinators addressed the project participants with"
    " a welcoming speech. In addition, regional centers of the Dance4Life"
    " Belarus project were established in Brest, Gomel, Grodno, and Mogilev."
    " Then, over the course of six days, the participants received competent"
    " knowledge in the field of HIV prevention, youth health and well-being,"
    " development of life skills, and countering health risks. The champions’"
    " training was carried out according to the “peer-to-peer” principle."
    " “Journey for Life” encompasses five stages of ten training modules of"
    " 1.5 hours each. The first stage, “Inspire,” focuses on creating a"
    " positive atmosphere and group dynamics. The second stage – “I,”"
    " is building personal confidence and self-esteem. The third one –"
    " “Me and You”- is about assessing one’s attitude towards others and"
    " developing interpersonal relationships. Then comes the segment –"
    " “Me and Society,” dedicated to existing social problems and the"
    " discovery of one’s role in society, the search for opportunities"
    " to change the world for the better. The final stage, “Celebrate,”"
    " is designed to celebrate the changes that have taken place and"
    " congratulate the new champions."
)

golden = (
    "In the autumn of 2022, the Belarusian Association of UNESCO Clubs"
    " launched the second stage of the Dance4Life Belarus project"
    " (“Journey4Life”) and conducted training to prepare a new"
    " generation of Champions4Life."
)

if __name__ == "__main__":
    result: dict[str, str] = requests.post(URL, json={"text": text}).json()
    print(result["summary"])
    assert result["summary"] == golden
    print("Success")
