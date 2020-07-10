def sumSquareDifference(n):
    sum_of_squares = (n*(n+1)/2)**2
    square_of_sum = n**3/3+n**2/2+n/6
    return sum_of_squares - square_of_sum

print(sumSquareDifference(100))
