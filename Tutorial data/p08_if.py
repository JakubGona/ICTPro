age = int(input("Zadejte svůj věk (celé číslo): "))

if age >= 18:
    print("Jsi dospělý.")
    print("Už můžeš jít makat.")
    print("Hurá.")
elif age >= 7:
    print("Nejsi dospělý.")
    print("Koukej se učit.")
    print("No hurá.")
else:
    print("Jdeme se dívat na pohádky.")

print("END")
