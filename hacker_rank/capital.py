import os
def solve(s):
    r, t = s.split(" ")
    r = r[0].upper() + r[1:]
    t = t[0].upper() + t[1:]
    print(r, t)



s = input()

solve(s)


