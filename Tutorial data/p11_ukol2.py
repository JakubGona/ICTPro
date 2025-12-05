"""
- uživatel zadá celé číslo
- pokud 0 => vypíšeme "Nula"
- pokud zadá kladné sudé číslo => "Kladné sudé číslo"
- pokud zadá kladné liché číslo => "Kladně liché číslo"
- pokud zadá záporné sudé číslo => "Záporné sudé číslo"
- pokud zadá záporné liché číslo => "Záporné liché číslo"

number > 0 => kladné
number < 0 => záporné

number % 2 == 0 => sudé
number % 2 == 1 => liché
"""

number = int(input("Zadej celé číslo: "))

if number == 0:
    print("Nula")
elif number > 0 and number % 2 == 0:
    print("Kladné sudé číslo")
elif number > 0 and number % 2 == 1:
    print("Kladně liché číslo")
elif number < 0 and number % 2 == 0:
    print("Záporné sudé číslo")
else:
    print("Záporné liché číslo")

print("="*80)

if number == 0:
    print("Nula")
elif number > 0:
    if number % 2 == 0:
        print("Kladné sudé číslo")
    else:
        print("Kladné liché číslo")
#elif number < 0:
else:
    if number % 2 == 0:
        print("Záporné sudé číslo")
    else:
        print("Záporné liché číslo")

print("="*80)

if number == 0:
    print("Nula")
elif number > 0:
    print("Kladné", end=" ")
else:
    print("Záporné", end=" ")
if number:
    if number % 2 == 0:
        print("sudé číslo")
    else:
        print("liché číslo")

