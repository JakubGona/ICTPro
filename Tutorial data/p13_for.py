for i in range(10):
    print(i, end=" ")

#print()
print("\n"+chr(10)+"="*80)

for i in range(2, 10):
    print(i, end=" ")

print()
print("="*80)

names = ["Adam", "Bára", "Cecil", "Dušan", "Eva", "Filip"]
for i in range(len(names)):
    print(names[i])

print("="*80)

for name in names:
    print(name)

print("="*80)
print("Vnořený for cyklus")

# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 ...
# ...

for i in range(1, 11):  # pro každý řádek
    for j in range(1, 11):  # pro každý sloupec v daném řádku
        #print(f"{i*j:03d}", end=" ")
        result = i*j
        if result < 10:
            print("  ", end="")
        elif result < 100:
            print(" ", end="")
        print(result, end=" ")
    print()  # na konci řádku přejdu na nový řádek
