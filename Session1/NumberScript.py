number = int(input("Zadaj celé číslo: "))

# Ak je číslo 0
if number == 0:
    print("Nula")

else:
    # Zistenie kladné / záporné
    if number > 0:
        sign = "Kladné"
    else:
        sign = "Záporné"

    # Zistenie párne / nepárne
    if number % 2 == 0:
        parity = "sudé"
    else:
        parity = "liché"

    # Výpis výsledku
    print(f"{sign} {parity} číslo")