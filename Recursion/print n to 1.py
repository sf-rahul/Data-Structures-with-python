#write a recursive function to print number from n to 1


#tail recursion : function call is the last thing.
#in tail recursion compiler user tail elimination that
#is it relaces functin call with go to 
def print_num(n):
    if n <=0:
        return 1;
    print(n)
    print_num(n-1)


#non tail recursion
#control goes to parent after child function finished.
#in the tail recursion control doesn't go to parent when child finishes.
def print_num_1_2_n(n):
    if n<=0:
        return 1
    print_num_1_2_n(n-1)
    print(n)


print_num(6)
        
print_num_1_2_n(6)


#printing 1 to n using tail recursion;

def tail_1_2_n(n,k=1):
    if n<=0:
        return 1
    print(k)
    tail_1_2_n(n-1,k+1)

print('1 to n using tail rec')
tail_1_2_n(6)
