my_set = {1, 2.5, 'a'}
print(f"my_set = {my_set}")  # my_set = {1, 2.5, 'a'}

my_set.add(5)
my_set.add(1)
print(f"my_set = {my_set}")  # my_set = {1, 2.5, 5, 'a'}

my_set.remove(2.5)
print(f"my_set = {my_set}")  # my_set = {1, 5, 'a'}

#print(f"my_set[0] = {my_set[0]}")  # TypeError: 'set' object is not subscriptable
print(f"1 in my_set: {1 in my_set}")

#my_set.