s = input()
width = int(input())
# for i in range(0, len(s)):
#     print(s[i:i+width])
#     i = i + width
i = 0

while i < len(s):
    print(s[i:i+width])
    i = i + width