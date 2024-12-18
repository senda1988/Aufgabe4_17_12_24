import datetime

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
