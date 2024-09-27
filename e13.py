import math

def tizenharmas():
    try:
        sugar = float(input("Add meg a kör sugarát:\n"))
        if sugar > 0:
            kerulet = 2 * math.pi * sugar
            terulet = math.pi * sugar ** 2
            print(f"A kör kerulete: {kerulet}, \nA kör területe: {terulet}")
        else:
            print("Hiba: a kör sugara nem pozitív!")
    except ValueError:
        print("Hiba: Nem valós számot adtál meg!")

tizenharmas()
