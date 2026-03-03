class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if (nums[i] + nums[j] == target):
                    print(f"[{i},{j}]")

r = Solution()
nums = list((input().split(" ")))
nums = [int(x) for x in nums]
target = int(input())
r.twoSum(nums,target)