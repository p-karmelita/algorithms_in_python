# import math
#
#
# def greatest_common_divisor(a, b):
#     if (b == 0):
#         return a
#     else:
#         return greatest_common_divisor(b, a % b)
#
#
# def is_prime(n):
#     if n <= 2:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if (n % i == 0):
#             return False
#     return True
#
# for i in range(2, 100):
#     if is_prime(i):
#         print(i, end=', ')
#
#
# def sieve_of_erastotenes(n):
#     tp = [True] * (n + 1)
#     i = 2
#     while i*i <= n:
#         if tp[i] == True:
#             for k in range(i * i, n + 1, i):
#                 tp[k] = False
#         i = i + 1
#     return tp
#
# res = sieve_of_erastotenes(100)
# print('\n\nCalculating prime numbers using Sieve of Erastotenes')
# for i in range(2, 100):
#     if res[i]:
#         print(i, end=', ')
#
#
# def showbits(s):
#     print(f'{s:3}=', end='')
#     weighs = [1, 2, 4, 8, 16, 32, 64, 128]
#     for i in range(7, -1, -1):
#         bit = weighs[i] & s
#         if bit != 0:
#             print('1', end='')
#         else:
#             print('0', end='')
#     print()
#
# showbits(5)
#
#
# tabl = [1, 2, 3, 2, -7, 44, 5, 0, -3]
# def search(tabl, left, right, x):
#     #x=value to search, left and right=left and right border of searching
#     if left > right:
#         print('Element ', x, ' wasn\'t found.')
#     else:
#         if tabl[left]==x:
#             print('Found searched element.')
#         else:
#             search(tabl, left+1, right, x)
#
# print('Table: ', tabl)
# search(tabl,0, len(tabl)-1, 3)
#
#
# def factorial(x):
#     if x==0:
#         return 1
#     else:
#         return x*factorial(x-1)
#
# for i in range(5, 11):
#     print(f'factorial({i})={factorial(i)}')
#
#
# def factorial2(x, tmp=1):
#     if x==0:
#         return tmp
#     else:
#         return factorial2(x-1, x*tmp)
#
# for i in range(5, 15):
#     print(f'factorial({i:2})={factorial(i):20} \t factorial2({i})={factorial2(i):20}')
#
#
# def fib(x):
#     if x < 2:
#         return x
#     else:
#         return fib(x - 1) + fib(x - 2)
#
# for i in range(1, 12):
#     print(f'fib({i})={fib(i)}')
#
#
# cpt = 0
# def mccarthy_function(x):
#     global cpt
#     cpt += 1
#     if x > 100:
#         return x-10
#     else:
#         return mccarthy_function(mccarthy_function(x+11))
#
# x = int(input('> set x: '))
#
# print(f'McCarthy({x}) = {mccarthy_function(x)}')
#
# if cpt==1:
#     print('[Function called once]')
# else:
#     print(f'[Function called {cpt} times]')
# print('Good bye!')
#
#
# tabl = [1, 2, 6, 7, 20, 18, 22, 25, 34, 39, 46]
#
#
# def recurent_binary_search(tab, x, left, right):
#     if left > right:
#         return -1                   # element not found
#     else:
#         mid = (left + right) // 2
#         if tab[mid] == x:
#             return mid              # element found
#         else:
#             if x < tab[mid]:         # search left
#                 return recurent_binary_search(tab, x, left, mid-1)
#             else:                   # search right
#                 return recurent_binary_search(tab, x, mid+1, right)
#
#
# print('Table: ', tabl)               # len() return size of table
# print('Searching for 39: ', recurent_binary_search(tabl, 39, 0, len(tabl)))


def reverse_array(tab, left, right):
    if left < right:
        tab[left], tab[right] = tab[right], tab[left]  # change extreme elements
        reverse_array(tab, left+1, right-1)            # reverse the rest


print('Table=', list(range(10)))
tabl = list(range(10))
reverse_array(tabl, 0, len(tabl)-1)
print('Table= ', tabl)
