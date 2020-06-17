from __future__ import print_function
#nth fibonacci using recursion
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return  fibo(n-1) + fibo(n-2)
    


#print(fibo(3))


#printing fibonacci terms in iterative way

def itr_fibo(n):
    last=1
    lst = [1]
    for i in range(0,n):
        sum = last+i
        last = i
        lst.append(sum)
    print(*lst,sep=" ")

#itr_fibo(3)

#printing fibonacci terms in recursive manner

fibonacci = {}
def fib(n):
    if n<=1:
        fibonacci[n]=n
        return n
    fib1= fibonacci[n-1] if n-1 in fibonacci else fib(n-1)
    fib2 = fibonacci[n-2] if n-2 in fibonacci else fib(n-2)
    fibonacci[n]=fib1+fib2
    if(fib1==1 and fib2==0):
        print(fib2)
        print(fib1)
    print(fib1+fib2)
    return fib1+fib2


fib(10)




    
    
    
    
    
    
    
        
        
        


