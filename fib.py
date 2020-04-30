# Fibonacci Sequence

# 1,1,2,3,5,8,13,21,34,55...

def fib(n):
    '''Will check the nth number in the fibonacci sequence'''

    assert type(n) == int, "'n' must be an integer"
    if n < 1:
        return "Invalid Input"
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(5)) # 5
print(fib(10)) # 55
print(fib(-3)) # "Invalid Input"
print(fib("1")) # AssertionError
