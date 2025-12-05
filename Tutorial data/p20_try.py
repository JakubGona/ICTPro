"""
num1 = int(input("Zadej první číslo: "))
num2 = int(input("Zadej druhé číslo: "))

if num2 == 0:
    print("To fakt ne.")
else:
    result = num1 / num2
    print(f"{num1}/{num2} = {result}")"""

try:
    num1 = int(input("Zadej první číslo: "))
    num2 = int(input("Zadej druhé číslo: "))

    result = num1 / num2
    print(f"{num1}/{num2} = {result}")
except ValueError as e:
    print(f"ERROR: máš chybu v hodnotě: {e}")
except ZeroDivisionError as e:
    print(f"ERROR: nulou neumím dělit: {e}")
except Exception as e:
    print(f"ERROR: {e}")
finally:
    print("END")
