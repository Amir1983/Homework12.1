import random

hauptstädte = {"Deutschland": "Berlin", "Frankreich": "Paris", "Ägypten": "Kairo", " Argentinien": "Buenos Aires", " Belgien": "Brüssel", "China": "Peking" }

while True:
    zufallsFrage = random.choice(list(hauptstädte.keys()))
    quizEingabe = input("Was ist die Hauptstadt von " + zufallsFrage + "?")
    if hauptstädte[zufallsFrage].lower() == quizEingabe.lower():
        print("Korrekt")
        break
    else:
        print("Leider Falsch!!!Neuer Versuch")
        continue
