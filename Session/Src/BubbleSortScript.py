# ANSI farby
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

numbers = [15, 20, 7, 3, 6, 11, 12]

n = len(numbers)

def print_highlighted(arr, idx1, idx2):
    """Vytlačí pole, kde indexy idx1 a idx2 sú farebné."""
    out = []
    for i, num in enumerate(arr):
        if i == idx1:
            out.append(f"{RED}{num}{RESET}")
        elif i == idx2:
            out.append(f"{YELLOW}{num}{RESET}")
        else:
            out.append(str(num))
    print(" ".join(out))

# Výpis pôvodného stavu
print(*numbers)
print()

for i in range(n - 1):
    for j in range(n - 1 - i):

        print_highlighted(numbers, j, j + 1)

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print()  # prázdny riadok po kole sortu

print(*numbers)