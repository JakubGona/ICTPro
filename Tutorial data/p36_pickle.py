import pickle

from p31_ukol9 import *

print(book1)

try:
    with open("book1.dat", 'wb') as f:
        pickle.dump(book1, f)
except Exception as e:
    print(e)

print("="*80)
try:
    with open("book1.dat", 'rb') as f:
        book1_copy = pickle.load(f)
        print(book1_copy)
except Exception as e:
    print(e)