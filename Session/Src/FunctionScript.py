def replace_str(text: str, old: str = " ", new: str = "_") -> str:
    return text.replace(old, new)

print(replace_str("Ahoj, jak se máš?"))

print(replace_str("Ahoj, jak se máš?", "j", "J"))