my_dict = {0: 'zero', 1: 'one', 2: 'two', 3: "three", '2': 'two'}
print(f"my_dict = {my_dict}")

print(f"my_dict[2]: {my_dict[2]}")
print(f"my_dict['2']: {my_dict['2']}")

numbers = {'nula': 'zero', 'jedna': 'one', 'dva': 'two', 'tři': 'three', 'tři': '3'}
print(f"numbers['tři'] = {numbers['tři']}")
numbers['tři'] = 'three'  # přepíšu stávající hodnotu
print(f"my_dict = {numbers}")
numbers['čtyři'] = 'four'  # přidám prvek
print(f"my_dict = {numbers}")

print(f"numbers.keys(): {numbers.keys()}"); print("KONEC")
