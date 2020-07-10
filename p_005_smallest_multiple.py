def smallestMult(n):
    lcm = 1
    i = 1
    while True:
        lcm = n * i
        j = 2
        while j<=n:
            if((lcm % j) != 0):
                break
            j+=1
        if(j-1==n):
            return n*i
        else:
            i+=1

print(smallestMult(10))