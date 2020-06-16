def palindrome(s,i,j):
    if i==j :
        return True
    if i>j :
        return True
    if s[i]!=s[j]:
        return False
    return palindrome(s,i+1,j-1)

s= input()
print(palindrome(s,0,len(s)-1))
    
    
