# Factorial
# 0! = 1
# 1! = 1
# 2! = 2 * 1 = 2
# 3! = 3 * 2 * 1 = 6

# n! = n * n - 1 * n - 2 ...

def factorial(n):
    assert type(n) == int, "'n' must be an integer"
    if n < 0:
        raise ValueError("Cannot find factorial of negative number")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # 120
print(factorial(1)) # 1
print(factorial(10)) # 3628800
print(factorial(-5)) # ValueError
print(factorial("abc")) # AssertionError
