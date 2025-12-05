"""
Součet čísel v seznamu.
Ošetřit na nečíselné hodnoty.
"""

my_list = [1, 2, 3, "4", "pět", 6]

result = 0

for number in my_list:
    try:
        result += number
    except:# TypeError as e:
        pass

print(result)