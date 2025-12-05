from requests import delete

a = 10
print(f"a: {a}, id: {id(a)}")
b = a
print(f"b: {b}, id: {id(b)}")

a = 20
print(f"a: {a}, id: {id(a)}")
print(f"b: {b}, id: {id(b)}")

print("="*80)
list_a = [1, 2.5, "three", ['a', 'b', 'c']]
print(f"list_a: {list_a}, id: {id(list_a)}")
list_b = list_a
print(f"list_b: {list_b}, id: {id(list_b)}")
list_a.append(3)
print(f"list_a: {list_a}, id: {id(list_a)}")
print(f"list_b: {list_b}, id: {id(list_b)}")

list_c = list_a.copy()
print(f"list_c: {list_c}, id: {id(list_c)}")

import copy
list_d = copy.deepcopy(list_a)
print(f"list_d: {list_d}, id: {id(list_d)}")

list_a[3].append('d')
print(f"list_a: {list_a}, id: {id(list_a)}")
print(f"list_b: {list_b}, id: {id(list_b)}")
print(f"list_c: {list_c}, id: {id(list_c)}")
print(f"list_d: {list_d}, id: {id(list_d)}")

# comment
# TODO: new task
# FIXME: change it!

print("="*80)
list_a[0] = 2
print(f"list_a: {list_a}, id: {id(list_a)}")
print(f"list_b: {list_b}, id: {id(list_b)}")
print(f"list_c: {list_c}, id: {id(list_c)}")
print(f"list_d: {list_d}, id: {id(list_d)}")
