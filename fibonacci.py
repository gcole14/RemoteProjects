import numpy as np

def fib(n):
    if n == 2 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

x = fib(2)
print(x)

def fib2(n):
    if n == 1 or n == 2:
        return 1
    x = [1, 1]
    for i in range(n-2):
        print(i)
        x = x + [x[-1]+x[-2]]
    return x[-1]

x = fib2(100)
print(x)