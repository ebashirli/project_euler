def sum_even_fibs(n):
    a = 0
    b = 1
    tot = 0
    while a<n:
        tot += a if a%2==0 else False
        tot += b if b%2==0 else False
        a += b
        b += a
    print(tot)

sum_even_fibs(10)