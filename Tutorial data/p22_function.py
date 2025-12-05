"""
fact(n) -> faktoriál čísla n
5! = 5*4*3*2*1 = 120
1! = 1
0! = 1
"""


def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    print("aaa")  # nedosažitelný kód


for i in range(11):
    print(f"{i}! = {fact(i)}")


print("="*80)


"""
Rekurze:
5! = 5*4!
"""

def fact_r(n):
    if n == 0:
        return 1
    result =  n * fact_r(n-1)
    #print(".", end="")
    return result


for i in range(11):
    print(f"{i}! = {fact_r(i)}")
