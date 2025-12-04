"""
Bubble sort

Zadaná čísla:
15 7 20 7 3 6 11 12 20
"""

numbers = [15, 7, 20, 7, 3, 6, 11, 12, 20]

print("Pôvodné čísla:")
print(numbers)

# Bubble sort
n = len(numbers)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # výpis po jednom "kole"
    print(numbers)

print("\nVýsledok (zoradené):")
print(numbers)