# Read inputs
N = int(input())
sizes = list(map(int, input().split()))
C = int(input())

total = 0

for _ in range(C):
    size_req, price = map(int, input().split())
    
    if size_req in sizes:
        total += price
        sizes.remove(size_req)  # remove sold shoe

print(total)
        