# cook your dish here
# cook your dish here


def findmin(n,m,d,pos,sum=0,index= 0):
    if index==n:
        left = findleft(n,d,pos)
        right = findleft(n,d,pos)
        sum = sum + left + right
        #print(m-sum)
        return m-sum 
    if(pos>0):
        d[pos]= 1 #only one or zero that's it.
        left = findleft(n,d,pos)
        right = findright(n,d,pos)
        sum += left + right
    lst =[]
    for key,value in d.items():
        if key>0 and key <n+1 and value==0:
            lst.append(findmin(n,m,d,key,sum,index+1))
    lst = list(filter(lambda x:x!=-1,lst))
        
    #lst = [findmin(m,d,pos+i,sum,index+1) for i in range(1,3-index+1)]  
    
        #a=findmin(m,d,pos+1,sum,index+1)
       #b=findmin(m,d,pos+2,sum,index+1)
       #c=fidmin(m,d,pos+3,sum,index+1)
    val = min(lst) if len(lst)!=0 else -1
    d[pos]=0
    return val
    
    
#pos 3 means third level in the recursion 3 , meaning 2 pos are filld.
def findleft(n,d,pos):
    if pos==1:
        return 1
    else:
        pos = pos-1
        k=0
        while pos>=0 and d[pos]==0:
            k=k+1
            pos=pos-1
        
        return k
        
    
        
def findright(n,d,pos):
    if pos==n:
        return 1
    else:
        k=0
        for i in range(pos+1,n+2):
            if d[pos]==0:
                k=k+1
            else:
                break
        return k
        
        

t = int(input())
while t>0:
    inputs = list(map(int,input().split()))
    n = inputs[0]
    m = inputs[1]
    pos=0
    d={}
    for  i in range(0,n+2):
        d[i]=0
    cost = findmin(n,m,d,pos,0,0)
    print(cost)
    t=t-1

#k,n-k+1   
#spot 1 to n
#pos=1 (the solderies order)

    
        
        
        
    
    
    
    
    
    


