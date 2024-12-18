import datetime
import calendar
import locale

locale.setlocale(locale.LC_ALL, "deu_deu")


def aktuelles_datum_und_uhrzeit():
    date_uhr = datetime.datetime.now()
    date_form = date_uhr.strftime("%d.%M.%Y %H:%M:%S")
    return date_form


def tage_bis_jahresende():
    heute = datetime.date.today()
    x = datetime.date(2024, 12, 31)
    anzahl_tage_bis_ende_jahr = x - heute
    return anzahl_tage_bis_ende_jahr


def tage_bis_datum():
    difference_tage = -1
    while difference_tage < 0:
        date_entry = input("Datum im Format TT.MM.JJJJ : ")
        try:
            datum = datetime.datetime.strptime(date_entry, "%d.%m.%Y").date()
            heute = datetime.date.today()
            difference = datum - heute
            difference_tage = difference.days
            if datum >= heute:
                print(f"{difference_tage}")

            else:
                print(difference_tage)
                print("Datum ist nicht gültig")
        except ValueError:
            print("Ungültiges Datum! Bitte das Datum im Format TT.MM.JJJJ eingeben.")


def wochentag_berechnen():
    date_entry = input("Datum im Format TT.MM.JJJJ : ")
    datum = datetime.datetime.strptime(date_entry, "%d.%m.%Y").date()
    return calendar.day_name[datum.weekday()]


def zeit_in_zukunft():
    jetz = datetime.datetime.now()
    date_entry = int(input("entry : 1- minuten, 2- stunden, 3- tagen "))

    if date_entry == 1:
        nbr = int(input(f"Wie viele minuten möchten Sie hinzufügen? "))
        min = datetime.timedelta(minutes=nbr)
        result = jetz + min
    elif date_entry == 2:
        nbr = int(input(f"Wie viele stunden möchten Sie hinzufügen? "))
        stunden = datetime.timedelta(hours=nbr)
        result = jetz + stunden
    elif date_entry == 3:
        nbr = int(input(f"Wie viele tagen möchten Sie hinzufügen? "))
        tage = datetime.timedelta(days=nbr)
        result = jetz + tage
    else:
        print("Error!")
    return result

    # time_zukunft= datetime.datetime.


def choice_funktion():
    choice = int(
        input(
            "wählen Sie ein Funktion: \n 1- aktuelles_datum_und_uhrzeit() \n 2- tage_bis_jahresende() \n 3- tage_bis_datum() \n 4- wochentag_berechnen() \n 5- zeit_in_zukunft()\n"
        )
    )
    if choice == 1:
        print(
            f"das aktuelle Datum und die aktuelle Uhrzeit im Format TT.MM.JJJJ HH:MM:SS  {aktuelles_datum_und_uhrzeit()}"
        )
    elif choice == 2:
        print(
            f"die Anzahl der Tage vom aktuellen Datum bis zum 31. Dezember ist : {tage_bis_jahresende()}"
        )
    elif choice == 3:
        print()
    elif choice == 4:
        print(f"Wochentag : {wochentag_berechnen()}")
    elif choice == 5:
        print(f"date zukunft : {zeit_in_zukunft()}")
    else:
        print("Error!")


choice_funktion()
