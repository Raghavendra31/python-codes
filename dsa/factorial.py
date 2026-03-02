def facto(data):
    r = 1
    for i in range (1,data+1):
        r = r*i
    return r
    
print(facto(10))