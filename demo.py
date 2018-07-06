import math


def factorielle(n):
    if n < 2:
        return 1
    else:
        return n * factorielle(n - 1)


def isprime(n):
    if n < 2:
        return False
    for i in range(2, round(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

#sans recursivité
"""def sum(tab):
    somme = 0
    for t in tab:
        somme += t
    return somme"""

#la même chose avec la recursivité
def sum(tab):
    if len(tab) == 1:
        return tab[0]
    else:
        return tab[len(tab)-1]+sum(tab[0:(len(tab)-1)])


def max(tab):
    max = tab[0]
    for t in tab:
        if t > max:
            max = t
    return max


def mean(tab):
    return sum(tab)/len(tab)


def getprime(tab):
    primetab = []
    for t in tab:
        if isprime(t):
            primetab.append(t)
    return primetab


def inverser(tab):
    for i in range(len(tab)-2, -1, -1):
        tab.append(tab[i])
        tab.remove(tab[i])
    return tab


x = 3
print(x)
s = "Hello world!"
print(s)
print(factorielle(5))
m = 3.14
print(f"Ceci est le nombre pi {m}")
print(isprime(4))
l2 = []
for i in range(10):
    l2.append(i)

print(*l2)
print(f"La somme de {l2} = {sum(l2)}")
print(f"Le max de {l2} = {max(l2)}")
print(f"Le moyen de {l2} = {mean(l2)}")
print(getprime(l2))
print(inverser(l2))
