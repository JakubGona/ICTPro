"""
Úkol 1:
- uživatel zadá výšku a váhu
- spočítame BMI
- na základě BMI vypíšte typ
"""

# Zadanie vstupov od užívateľa
vyska = float(input("Zadajte výšku v metroch (napr. 1.80): "))
vaha = float(input("Zadajte váhu v kilogramoch: "))

# Výpočet BMI
bmi = vaha / (vyska ** 2)

print(f"\nVaše BMI je: {bmi:.2f}")

# Určenie kategórie BMI
if bmi < 18.5:
    print("➡️ Typ: Podváha")
elif bmi < 25:
    print("➡️ Typ: Normálna váha")
elif bmi < 30:
    print("➡️ Typ: Nadváha")
else:
    print("➡️ Typ: Obezita")