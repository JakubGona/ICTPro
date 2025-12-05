"""
napište funkci is_prime, která má na vstupu jedno číslo a vrací
True, pokud je to prvočíslo
False, pokud to není prvočíslo
"""

def is_prime(n: int) -> bool:
    #count = 0
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # pokud najdu dělitele od 2 do n, tak to není prvočíslo -> False
    for i in range(3, int(n**(1/2)+1), 2):
        #count += 1
        if n % i == 0:
            #print(f"Proběhlo {count} iterací")
            return False
    # jinak -> je to prvočíslo -> True
    #print(f"Proběhlo {count} iterací")
    return True

#print(is_prime(1.7))
#print(is_prime(997))
for i in range(20):
    print(f"{i}: {is_prime(i)}")

"""
Napište funkci primes_to_n(n), která vrátí seznam všech prvočísel menších nebo rovno hodnotě n
primes_to_n(20) -> [2, 3, 5, 7, 11, 13, 17, 19] 
"""


def primes_to_n(n):
    result = []
    for i in range(n+1):
        if is_prime(i):
            result.append(i)
    return result


print(primes_to_n(100))
