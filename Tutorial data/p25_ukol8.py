"""
Napište funkci replace_str(text: str, old: str, new: str), která bude mít v argumentech:
text -> původní text
old -> co chci nahradit
new -> čím to chci nahradit
Chceme použít defaultní hodnoty, old=" ", new="_", ale jsem schopný to změnit.
Např.
replace_str("Ahoj, jak se máš?") -> "Ahoj,_jak_se_máš?"
replace_str("Ahoj, jak se máš?", "j", "J") -> "AhoJ, Jak se máš?"
"""

def replace_str(text: str, old: str = " ", new: str = "_") -> str:
    return text.replace(old, new)


print(replace_str("Ahoj, jak se máš?"))
print(replace_str("Ahoj, jak se máš?", "j", "J"))
