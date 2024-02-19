import functools

print("hello")
print("World")

def factorial(n):
    return functools.reduce(lambda a,b: a*b, range(1, n+1))