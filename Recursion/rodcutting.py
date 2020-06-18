#problem: Given a rope of length n ,you need to find maximum no of pieces you can make,
#such that the length of every piece is in set {a,b,c} for given three values of a,b,c

#i/p : n=5, a=2,b=5,c=1  o/p = 5
#i/p : n=23,a=12,b=9,c=11  o/p=2
#i/p : n=5 , a=4,b=2,c=6 o/p=-1

#(n,{a,b,c}) = max((n,a),(n,b),(n,c),(n,a,b),(n,b,c),(n,a,c),(n,a,b,c))

def rod_cutting(n,a,b,c):
    if n<0:
        return -1
    if n==0:
        return 0
    pieces = max([rod_cutting(n-i,a,b,c) for i in [a,b,c]])

    return -1 if pieces <0 else 1+pieces

print(rod_cutting(23,12,9,11))

#time complexity : O(3**n)