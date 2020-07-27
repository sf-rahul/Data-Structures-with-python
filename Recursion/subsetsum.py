# cook your dish here
t = int(input())
while t>0:
    n = int(input())
    lst = list(map(int,input().split()))
    d= {}
    l = []
    q= False
    for i in range(0,n):
        k = [0]*n
        k[i]=lst[i]|lst[i]
        if k[i] in d:
            q=True
            break
        d[k[i]]=1
        l.append(k)
    if q==False:
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                l[i][j]=l[i][j-1]|lst[j]
                if l[i][j] in d:
                    q=True
                    break
                d[l[i][j]] =1
    if not q:
        print('YES')
    else:
        print('NO')
    #print(len(d.keys()))
            
    t = t-1
