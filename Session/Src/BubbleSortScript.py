"""
Bubble sort – s výpisom porovnávaných čísel
"""

numbers = [15, 20, 7, 3, 6, 11, 12]

n = len(numbers)

# Pôvodný stav
print("Pôvodné čísla:")
print(*numbers)
print()

for i in range(n - 1):
    for j in range(n - 1 - i):

        # výpis porovnávaných čísel
        print(f"Porovnávam: {numbers[j]} a {numbers[j+1]}")

        # ak je ľavé väčšie → prehodíme
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        # výpis po porovnaní/výmene
        print(*numbers)
        print()

    print("Koniec kola", i + 1)
    print()

print("Výsledok:")
print(*numbers)