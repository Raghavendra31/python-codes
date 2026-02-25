ragu = input()
nums = list(map(int, ragu.strip("[]").split(",")))


target = int(input())

for i in range( 0,len(nums)):
    for j in range( 0,len(nums) ):
        if (nums[i] + nums[j] == target):
            print (f"[{i},{j}]")

