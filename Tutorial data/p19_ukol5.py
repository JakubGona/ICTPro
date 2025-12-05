"""
Hledání odmocniny s přesností na 3 desetinná místa:

Uživatel zadá číslo (> 1): n (např. 5)
My víme, že hledaná odmocnina bude někde v intervalu (1, n)
Najdeme prostřední číslo z daného intervalu s = (n+1)/2  (3)
Spočítám druhou mocninu s ** 2 (9)
Na začátku mám inteval (1, 5)
1 2 3 4 5
    3      -> 3 ** 2 = 9 -> to je moc -> zmenším interval na (1, 3)
1 2 3
  2        -> 2 ** 2 = 4 -> to je málo -> zmenším interval na (2, 3)
  2 3
  2.5      -> 2.5 ** 2 = 6.25 -> to je moc -> zmenším interval na (2, 2.5)
  2 2.5
  2.25     -> 2.25 ** 2 = 5.06 -> to je moc -> zmenším interval na (2, 2.25)
atd...
"""
from locale import locale_encoding_alias

number = float(input("Zadej číslo větší než 1: "))

lower_limit = 1
upper_limit = number
middle = (lower_limit + upper_limit) / 2

while abs(middle ** 2 - number) > 0.001:
    middle = (lower_limit + upper_limit) / 2
    if middle ** 2 > number:
        # dolní mez nechám
        upper_limit = middle  # změním horní limit na prostřední hodnotu
    else:
        lower_limit = middle  # změním dolní limit na prostřední hodnotu
        # horní mez nechám
    #print(f"middle = {middle}, lower = {lower_limit}, upper = {upper_limit}")
print(f"Odmocnina z {number} = {round(middle, 3)}.")
