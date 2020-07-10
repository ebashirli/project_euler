def largest_palindrome_product(n):
    n_digit_nine = 9 * int("1"*n)
    for i in range(n_digit_nine, n_digit_nine-9 * int("1"*(n-1)),-1):
        for j in range(n_digit_nine, n_digit_nine - 9 * int("1"*(n-1)), -1):
            if(str(i*j)[::-1]==str(i*j)):
                return i*j

print(largest_palindrome_product(3))