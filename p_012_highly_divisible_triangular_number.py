def divisibleTriangleNumber(n):
    next_triangle_number = 0
    number_of_divisor = 0
    i = 0
    while True:
        next_triangle_number += i
        for j in range(1, int(next_triangle_number ** 0.5)):
            if (next_triangle_number % j) == 0:
                number_of_divisor += 1
        if (number_of_divisor * 2) > n:
            return next_triangle_number
        number_of_divisor = 0
        i+=1

print(divisibleTriangleNumber(23))
