""" Úkol 1:
- uživatel zadá výšku a váhu
- spočítáme BMI
- na základě BMI vypište typ
"""

vyska = int(input("zadejte vysku (cm): "))
vaha = int(input("zadejte vahu (kg): "))
vyskam = vyska / 100
bmi = (vaha / (vyskam ** 2))
print(bmi)

if bmi < 18.5:
    print("podvaha")
elif bmi < 25:
    print("normalni vaha")
elif bmi < 30:
    print("nadvaha")
elif bmi < 35:
    print("obezita 1")
else:
    print("obezita 2")
