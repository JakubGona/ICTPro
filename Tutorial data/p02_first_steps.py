number1 = 5  # int
print(f"{number1}")

number1 = 5.7  # float
print(f"{number1}")

number1 = "five"
print(number1)

num1: int = 5
num2: int = 7
result = num1 + num2
print(result)
print(f"{num1} + {num2} = {result}")  # 5 + 7 = 12

num1 = 3.7
print(f"{num1}")

print("="*80)
#age = input("What is your age? ")  # age is string!
#age = int(age)  # age is int
#print(f"Your age is {age}.")
age = int(input("What is your age? "))  # age is int
print(f"Your age is {age}.")

print("="*80)
print("Text")
print('Text')

name = "Petr"
print(f"My name is '{name}'.")
print(f'My name is "{name}".')

text = """First row.
Second row.
Third row."""
print(text)
# comment
"""
print("="*80)
print("Text")
print('Text')"""

name = "Petr"
surname = "Gregor"
full_name = name + " " + surname  # Petr Gregor
print(full_name)

print(full_name * 3)
print(full_name[0])
print(f"Iniciály: {"-"*9} {name[0]}{surname[0]}")
print(f"Poslední znaky: {name[-1]}{surname[-1]}")

my_text = "First line\n\tSecond line\n\t\tThird line"
print(my_text)

print("我叫彼得。")

我 = 5
print(我)

jméno = "Petr"
print(jméno)

print("="*80)
name = "Petr"
print(name.upper())  # PETR
print(name)
print(name.lower())  # petr
print(name.title())  # Petr

name = "    Petr    "
print(f"'{name}'")
print(f"'{name.strip()}'")

name = "Petr"
print(name.startswith("Pe"))

number = "0123456789"
print(number.isdigit())

text = "Hello Petr, how are you?"
texts = text.split(" ")
print(texts)

num3 = "019"
print(num3.isnumeric())
print(int(num3))
