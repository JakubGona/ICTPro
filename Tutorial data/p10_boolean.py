_true = True
_false = False
_none = None

print(f"_true = {_true}, _false = {_false}")

# and => pravda, pokud jsou obě podmínky pravdivé
# True and True => True
# True and False => False
# False and True => False
# False and False => False
print(f"_true and _true = {_true and _true}")    # True
print(f"_true and _false = {_true and _false}")  # False
print(f"_none and _false = {_none and _false}")  # None
print(f"_false and _none = {_false and _none}")  # False

my_list = [1, 2]
if len(my_list) > 10 and my_list[10] > 10:
    print("Větší než 10.")


# or => pravda, pokud je alespoň jedna podmínka pravdivá
# True or True => True
# True or False => True
# False or True => True
# False or False => False
print(f"_true or _false = {_true or _false}")
print(f"_false or _false = {_false or _false}")

# lze kombinovat
print(f"_true and (_false or _true) = {_true and (_false or _true)}")
