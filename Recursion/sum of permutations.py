import math
def getSum(n, arr):
    #Code here
    f = math.factorial(n-1)
    term = sum(arr)*f
    p=1
    res=0
    for i in range(1,n+1):
        res += (term*p)
        p *= 10
    
    return res
