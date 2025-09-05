nums = list(map(int, input().split()))
target = int(input())
print(nums)
for num in range(len(nums)):
    if (num + 1) in range(len(nums)):
        for n in range(len(nums)):
            if (n+1) in range(len(nums)):
                output = nums[num] + nums[n+1]
                if output is target:
                    print(f"[{num},{n+1}]")

