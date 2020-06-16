#factorial usign recursion

#head recursion
def fact_head(n):
    if n <=1:
        return 1;
    return n*fact_head(n-1)

print('head recursin',fact_head(6))


#tail recursion

def fact_head(n,val=1):
    if n<=1:
        return val
    return fact_head(n-1,n*val)

print('tail recursion' , fact_head(6))
