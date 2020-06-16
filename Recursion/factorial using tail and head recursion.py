#factorial usign recursion

#head recursion
def fact_head(n):
    if n <=1:
        return 1;
    return n*fact_head(n-1)

print('head recursin',fact_head(6))


#tail recursion
#doesn't need to maintain states.

def fact_head(n,val=1):
    if n<=1:
        return val
    print(n,val)
    return fact_head(n-1,n*val)


#fact_head(5, 1)
#fact_head(4, 5*1)
#fact_head(3, 4*5*1)
#fact_head(2, 3*4*5*1)
#fact_head(1, 2*3*4*5*1)
#120

print('tail recursion' , fact_head(6))


