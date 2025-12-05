i = 0
while i < 5:
    print(i)
    i += 1

print("="*80)

my_number = 27
user_tip = int(input("Hádej číslo: "))
while user_tip != my_number:
    #user_tip = int(input("Špatně, hádej znovu: "))
    if user_tip < my_number:
        user_tip = int(input("Špatně, moje číslo je větší. Hádej znovu: "))
    else:
        user_tip = int(input("Špatně, moje číslo je menší. Hádej znovu: "))
print("Správně, uhodl jsi moje číslo.")