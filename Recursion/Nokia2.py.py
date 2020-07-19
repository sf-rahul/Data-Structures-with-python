def findcost(m,n,sum=0):
    if n==0:
        return sum if m-sum>=0 else -1
    if n==1:
        sum = sum+2
        return sum if  m-sum >=0  else -1
    if n==2:
        sum=sum+5
        return sum if  m-sum >=0 else -1
    lst = []
    sum += n+1
    for k in range(1,n+1):
        lst.append(partition(m,n,k,sum))
    #print(lst)
    lst = list(filter(lambda x:x!= -1, lst))
    
    return max(lst) if len(lst)>0 else -1
        
def partition(m,n,k,sum):
    t1 = findcost(m,k-1,sum)
    t2 = findcost(m,n-k,t1) if t1>0 else -1
    return t2 if t2 > 0 else -1
    
    
t = int(input())
while t>0:
    inputs = list(map(int,input().split()))
    n = inputs[0]
    m = inputs[1]
    #print(n,m)
    result = findcost(m,n,0)
    if result >=0 :
        print(m-result)
    else:
        print(-1)
    t=t-1

#k,n-k+1   
#spot 1 to n
#pos=1 (the solderies order)

    
        
        
        
    
    
    
    
    
    


