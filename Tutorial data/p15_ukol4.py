"""
Bubble sort

15 20 7 3 6 11 12
15 7 20 3 6 11 12
15 7 3 20 6 11 12
15 7 3 6 20 11 12
15 7 3 6 11 20 12
15 7 3 6 11 12 20

15 7 3 6 11 12 20
7 15 3 6 11 12 20
7 3 15 6 11 12 20
"""

"""
num1 = 10
num2 = 20
print(f"num1 = {num1}, num2 = {num2}")

#tmp = num1
#num1 = num2
#num = tmp

num1, num2 = num2, num1
print(f"num1 = {num1}, num2 = {num2}")
"""

numbers = [15, 20, 7, 3, 6, 11, 12]

#numbers = [5, 6, 7, 8, 20, 0]

changes = 0

for _ in range(len(numbers)):
    #print(_)
    changes = 0
    for i in range(len(numbers)-1-_):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            #changes = changes + 1
            changes += 1
    if changes == 0:
        break
print(numbers)

print("="*80)

numbers = [15, 20, 7, 3, 6, 11, 12]
changes = 5
while changes > 0:
    changes = 0
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            changes += 1
print(numbers)