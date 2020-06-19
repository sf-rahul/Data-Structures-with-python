#given a string print all subsets of it 
#i/p: "ABC"
#o/p: "","A","B","C","AB","BC","ABC"

#use combinatorial search optimization.

def subsets(s,st="",index = 0):
    if index==len(s):
        print(st)
        return
    else:
        subsets(s,st,index+1)
        subsets(s,st+s[index],index+1)
        
    
    

subsets("ABCDEFG")