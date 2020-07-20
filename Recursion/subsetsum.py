#finding no of subset exists having sum equal to given number:
def subsetsum(arr,n,s):
    if n==0:
        return 1 if s==0 else 0
    return subsetsum(arr,n-1,s) + subsetsum(arr,n-1,s-arr[n-1])
print(subsetsum([5,3,2,6],4,8))
