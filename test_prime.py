import math

def primeList(n):
    primes = []
    compteur = 1
    if n > 1:
        compteur += 1
        primes.append(2)
    for i in range(3, n+1):
        check = True
        for p in primes:
            compteur += 1
            if i % p == 0:
                check = False
                break
        if check:
            primes.append(i)
    return primes, compteur


def isprime(n, c):
    check = True
    if n < 2:
        c += 1
        check = False
    for i in range(2, round(math.sqrt(n))+1):
        c += 1
        if n % i == 0:
            check = False
    return check, c


def getprime(tab):
    primetab = []
    c = 1
    for t in tab:
        check, c = isprime(t, c)
        if check:
            primetab.append(t)
        c += c
    return primetab, c


power = 0
n = 1#10**power
primes = []
primes, compteur = primeList(n)
print(f"{100*len(primes)/n} primes in 10^{power} in {compteur} steps")
tab = []
for i in range(n):
    tab.append(i)
primes2, compteur2 = getprime(tab)
print(f"{100*len(primes2)/n}% of primes in 10^{power} in {compteur2} steps")
