# Aufgabe 3: Programmierübungen vom Vormittag
def cal_area(width, height):
    return width * height


def miles_to_kilometers(m):
    return m * 1.60934


def kilometers_to_miles(km):
    return km / 1.60934


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def funktion():
    choice = input(
        "wählen Sie eine funktion: \n 1: calc_area \n 2: Miles to kilometers \n 3: kilometers to miles \n 4: celsius to fahrenheit \n"
    )
    list_choice = ["1", "2", "3", "4"]
    if choice in list_choice:
        if choice == "1":
            width = float(input(" width please: "))
            height = float(input(" height please: "))
            print(f" area = {cal_area(width, height)}")
        elif choice == "2":
            mile = float(input(" Miles:"))
            print(f"Miles -> kilometer: {miles_to_kilometers(mile)} ")
        elif choice == "3":
            km = float(input("kilometers:"))
            print(f"kilometer -> Miles : {kilometers_to_miles(km)}")
        else:
            cel = float(input("celsius: "))
            print(f"celsius to Fahrenheit : {celsius_to_fahrenheit(cel)}")
    else:
        print("choice Invalid !")


funktion()
