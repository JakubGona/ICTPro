""" Úkol 3
Vytvořte tabulku, kde v řádcích budou hodnoty od -10 do 20, ve sloupcích:
°C  °F °K
-10 ??
-9  ??
-8  ??
..
20

BONUS: Uživatel zadá rozsah hodnot v tabulce (např. od 0 do 100)

°F = (°C*1.8) + 32
°K = °C + 273.15
"""

start = int(input("Zadej minimální teplot (°C): "))
stop = int(input("Zadej maximální teplotu (°C): "))

print("°C\t\t°F\t\t°K")
print("-"*22)
width = 5
for c in range(start, stop+1):
    print(f"{c:3d}\t\t{(c*1.8) + 32:{width}.1f}\t{c+273.15}")
