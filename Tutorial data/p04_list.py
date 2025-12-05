my_list = [1]
print(my_list)  # [1]

my_list.append(2)
print(my_list)  # [1, 2]

my_list.append(3)
print(my_list)  # [1, 2, 3]

my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]

last = my_list.pop()
print(f"last = {last}")
print(my_list)  # [1, 2, 3, 4, 5]

first = my_list.pop(0)
print(f"first = {first}")
print(my_list)  # [2, 3, 4, 5]

my_list.remove(3)
print(my_list)  # [2, 4, 5]

#my_list.remove(3)  # ValueError: list.remove(x): x not in list
my_list.insert(1, 3)
print(my_list)  # [2, 3, 4, 5]

print(f"my_list[1] = {my_list[1]}")  # my_list[1] = 3
print(f"my_list[-1] = {my_list[-1]}")  # my_list[-1] = 5

print("=== Slicing ===")
#       0    1    2    3    4    5    6    7    8
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#     0    1    2    3    4    5    6    7    8    9
print(f"abc[6] = {abc[6]}")
print(f"abc[2:6] = {abc[2:6]}")  # abc[2:6] = ['c', 'd', 'e', 'f']
print(f"abc[2:] = {abc[2:]}")  # abc[2:] = ['c', 'd', 'e', 'f', 'g', 'h', 'i']
print(f"abc[:5] = {abc[:5]}")  # abc[:5] = ['a', 'b', 'c', 'd', 'e']
print(f"abc[:] = {abc[:]}")  # abc[:] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(f"abc[1:7:2] = {abc[1:7:2]}")  # abc[1:7:2] = ['b', 'd', 'f']
print(f"abc[1:7:-1] = {abc[1:7:-1]}")  # abc[1:7:-1] = []
print(f"abc[::-1] = {abc[::-1]}")  # abc[::-1] = ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

print(f"abc[2] = {abc[2]}")  # 'c'
print(f"abc[2:3] = {abc[2:3]}")  # ['c']

print(f"Length of abc: {len(abc)}")
