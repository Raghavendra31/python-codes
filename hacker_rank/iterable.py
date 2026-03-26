def itertool1(s,r):
    for i in range(len(s)):
        for j in range(len(r)):
            print(f"({s[i]}, {r[j]})", end = " ")
            

s = (input().split(" "))

r = (input().split(" "))

itertool1(s,r)