# import os
# def solve(s):
#     r, t = s.split(" ")
#     r = r[0].upper() + r[1:]
#     t = t[0].upper() + t[1:]
#     print(r, t)



# s = input()

# solve(s)

def merge_the_tools(string, k):
    n = len(string)
    
    for i in range(0,n,k):
        substring = string[i:i+k]
        s = set() 
        result = ""
        
        for char in substring:
            if char not in set:
                set.add(char) 
                result += char  
        print(result)    


merge_the_tools("raguarhuq",3)
    
