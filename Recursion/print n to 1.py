#write a recursive function to print number from n to 1

def print_num(n):
    if n <=0:
        return 1;
    print(n)
    print_num(n-1)

print_num(6)
        
