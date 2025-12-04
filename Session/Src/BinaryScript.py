n = float(input("Zadaj číslo (>1): "))

left = 1
right = n

while (right - left) > 0.001:  # presnosť na 3 desatinné miesta
    mid = (left + right) / 2
    square = mid * mid

    # rozhodnutie podľa veľkosti
    if square > n:
        right = mid
    else:
        left = mid

# výpis zaokrúhlený na 3 desatinné miesta
root = (left + right) / 2
print(f"Odmocnina z {n} je približne: {root:.3f}")