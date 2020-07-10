def multiplies_of_3_or_5(number):
    return sum([i for i in range(number) if (i % 3 == 0 or i % 5 == 0)])

