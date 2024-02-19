import functools

def factorial(n):
    return functools.reduce(lambda a,b: a*b, range(1, n+1))