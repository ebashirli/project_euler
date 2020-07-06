def largest_prime_factor(number):
    largest_prime = 1
    prime = 2
    while prime<=number:
        if number%prime==0:
            largest_prime = prime
            number/=prime
        else:
            prime+=1
    return largest_prime

print(largest_prime_factor(600851475143))