def nthPrime(n):
  primes = [2,3]
  number = 5
  while len(primes) < n:
    isPrime = False
    i = 1
    while primes[i] <= number ** 0.5:
      if number%primes[i]==0:
        isPrime = True
        break
      i+=1
    primes.append(number) if isPrime == False else False
    number += 2
  return primes[n-1]

print(nthPrime(100000001))