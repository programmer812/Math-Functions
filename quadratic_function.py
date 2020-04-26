def quadratic_function(a, b, c):
    assert type(a) == int, "Please input integer numbers"
    assert type(b) == int, "Please input integer numbers"
    assert type(c) == int, "Please input integer numbers"
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    else:
        if (b ** 2) - (4 * a * c) < 0:
            raise ValueError("Cannot square root a negative number")
        elif (b ** 2) - (4 * a * c) == 0:
            x = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / 2 * a
            return x
        else:
            print("There are two real roots")
            x = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / 2 * a
            y = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / 2 * a
            return x,y

print(quadratic_function(1, 4, 4))
print(quadratic_function(0, 4, 4))
print(quadratic_function(10, 1, 10))
