# Aufgabe 4: Schere Stein Papier
import random


def schere_stein_papier():
    Spiel_nochmal = "ja"
    nb_user_gewin = 0
    nb_comp_gewin = 0
    runde = 0

    while Spiel_nochmal == "ja":
        choice = input(
            "Was wählen Sie? \n 1- Schere \n 2- Stein \n 3- Papier \n "
        ).lower()
        while choice not in ["schere", "stein", "papier"]:
            choice = input("Was wählen Sie? \n 1- Schere \n 2- Stein \n 3- Papier \n ")

        choice_computer = random.choice(["Schere", "Stein", "Papier"]).lower()
        print(f"Du hast gewählt: {choice}")
        print(f"Der Computer hat gewählt: {choice_computer}")
        if choice == choice_computer:
            print("nochmal Wählen")
        elif (
            (choice == "schere" and choice_computer == "papier")
            or (choice == "stein" and choice_computer == "schere")
            or (choice == "papier" and choice_computer == "stein")
        ):
            print("der User gewinnt")
            nb_user_gewin = nb_user_gewin + 1
        else:
            print("der Computer gewinnt")
            nb_comp_gewin = nb_comp_gewin + 1
        runde += 1
        Spiel_nochmal = input("Wollen Sie nochmal spielan? Ja / Nein ").lower()

    print(f"user giwinnt {nb_user_gewin} mal und computer gewinnt {nb_comp_gewin} mal")
    print(f"Anzahl Runden : {runde}")


schere_stein_papier()
