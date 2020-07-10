def primeSummation(n):
    from functools import reduce
    if n<2:
        return 0
    elif n == 3:
        return 2
    else:
        primes = [2,3]

        number = 5

        while number < n:
            isPrime = False
            i = 1
            while primes[i] <= number ** 0.5:
                if number % primes[i] == 0:
                    isPrime = True
                    break
                i += 1
            primes.append(number) if isPrime == False else False
            number += 2

        return reduce(lambda a, b: a+b, primes)

print(primeSummation(2))