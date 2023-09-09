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


def showbits(s):
    print(f'{s:3}=', end='')
    weighs = [1, 2, 4, 8, 16, 32, 64, 128]
    for i in range(7, -1, -1):
        bit = weighs[i] & s
        if bit != 0:
            print('1', end='')
        else:
            print('0', end='')
    print()

showbits(5)


tabl = [1, 2, 3, 2, -7, 44, 5, 0, -3]
def search(tabl, left, right, x):
    #x=value to search, left and right=left and right border of searching
    if left > right:
        print('Element ', x, ' wasn\'t found.')
    else:
        if tabl[left]==x:
            print('Found searched element.')
        else:
            search(tabl, left+1, right, x)

print('Table: ', tabl)
search(tabl,0, len(tabl)-1, 3)


def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)

for i in range(5, 11):
    print(f'factorial({i})={factorial(i)}')


def fib(x):
    if x < 2:
        return x
    else:
        return fib(x - 1) + fib(x - 2)

for i in range(1, 12):
    print(f'fib({i})={fib(i)}')


cpt = 0
def mccarthy_function(x):
    global cpt
    cpt += 1
    if x > 100:
        return x-10
    else:
        return mccarthy_function(mccarthy_function(x+11))

x = int(input('> set x: '))

print(f'McCarthy({x}) = {mccarthy_function(x)}')

if cpt==1:
    print('[Function called once]')
else:
    print(f'[Function called {cpt} times]')
print('Good bye!')
