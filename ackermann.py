def ackermann_function(m, n):
    if m == 0:
        return n + 1
    else:
        if m > 0 and n == 0:
            return ackermann_function(m - 1, 1)
        else:
            if m > 0 and n > 0:
                return ackermann_function(m - 1, ackermann_function(m, (n - 1)))


# testujemy program
while True:
    try:
        m = int(input('input m: '))
        n = int(input('input n: '))
        break
    except ValueError:
        print('error try again')

print(f'A({m}, {n}) = {ackermann_function(m, n)}')
