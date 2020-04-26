def quadratic_function(a, b, c):
    if a == 0:
        print("Denominator cannot be 0")
    else:
        if (b ** 2) - (4 * a * c) < 0:
            print("Cannot square root a negative number")
        elif (b ** 2) - (4 * a * c) == 0:
            print("There is one real root")
            x = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / 2 * a
            print(x)
        else:
            print("There are two real roots")
            x = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / 2 * a
            y = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / 2 * a
            print(x,y)

quadratic_function(1, 4, 4)
quadratic_function(0, 4, 4)
quadratic_function(10, 1, 10)
