name = input("Zadej svoje jméno: ")

# Adam, Bára, Ctirad, Dana, Eva

if name == "Adam":
    print("Ahoj Adame.")
elif name == "Bára":
    print("Ahoj Báro")
elif name == "Ctirad":
    print("Ahoj Ctirade")
elif name == "Dana":
    print("Ahoj Dano")
elif name == "Eva":
    print("Ahoj Evo")
else:
    print("Ahoj")

print("="*80)

match name:
    case "Adam": # | "Aleš":
        print("Ahoj Adame.")
    case "Bára":
        print("Ahoj Báro")
    case "Ctirad":
        print("Ahoj Ctirade")
    case "Dana":
        print("Ahoj Dano")
    case "Eva":
        print("Ahoj Evo")
    case _:
        print("Ahoj")