def largeSum(arr):
    from functools import reduce
    return str(reduce(lambda a,b: int(a)+int(b), arr))[:10]

testNums = [
        '37107287533902102798797998220837590246510135740250',
        '46376937677490009712648124896970078050417018260538'
        ]

print(largeSum(testNums))