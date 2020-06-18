def sumofdigit(n):
    if n==0:
        return 0
    return sumofdigit(n//10)+n%10


print(sumofdigit(123456))