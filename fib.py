# Fibonacci Sequence

# 1,1,2,3,5,8,13,21,34,55...

def fib(n):
    if n < 1:
        return "Invalid Inputs"
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(5)) # 5
print(fib(10)) # 55
print(fib(-3)) # "Invalid Input"
