import math


def greatest_common_divisor(a, b):
    if (b == 0):
        return a
    else:
        return greatest_common_divisor(b, a % b)


def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

for i in range(2, 100):
    if is_prime(i):
        print(i, end=', ')


def sieve_of_erastotenes(n):
    tp = [True] * (n + 1)
    i = 2
    while i*i <= n:
        if tp[i] == True:
            for k in range(i * i, n + 1, i):
                tp[k] = False
        i = i + 1
    return tp

res = sieve_of_erastotenes(100)
print('\n\nCalculating prime numbers using Sieve of Erastotenes')
for i in range(2, 100):
    if res[i]:
        print(i, end=', ')
        