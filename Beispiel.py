# from datetime import datetime, date


# def tage_bis_datum():
#     date_entry = input("Bitte ein Datum im Format TT.MM.JJJJ eingeben: ")
#     datum = datetime.strptime(date_entry, "%d.%m.%Y").date()
#     # aktuelle datum
#     datum_heute = datetime.today().date()
#     difference = datum - datum_heute
#     return print(f"difference: {difference.days}")


# tage_bis_datum()


# def wochentag_berechnen():
#     datum_entry = input("Bitte ein Datum im Format TT.MM.JJJJ eingeben: ")
#     datum = datetime.strptime(datum_entry, "%d.%m.%Y").date()
#     wochentag = [
#         "Montag",
#         "Dienstag",
#         "Mittwoch",
#         "Donnerstag",
#         "Freitag",
#         "Samstag",
#         "Sonntag",
#     ]
#     return wochentag[datum.weekday()]


# print(f" Der Wochentag ist {wochentag_berechnen()}")


zahlen = [1, 2, 3, 4, 5]
print("Die erste Zahl ist:", zahlen[0])
print("Die letzte Zahl ist:", zahlen[-1])
