def print_user_info(name: str, surname: str, age: int) -> None:
    print(f"name={name}, surname={surname}, age={age}")


# poziční argumenty -> přiřazují se v daném pořadí
print_user_info("Petr", "Gregor", 30)

# klíčové/pojmenované argumenty -> nezáleží na pořadí
print_user_info(surname="Novák", age=25, name="Adam")


def print_message(message: str, important=False) -> None:
    if important:
        print(message.upper())
    else:
        print(message)

print_message("Ahoj")
print_message("Error", important=True)
print_message("Warning", important=False)