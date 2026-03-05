class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

r = Solution()

nums = eval(input())   # converts "[2,7,11,15]" → [2,7,11,15]
target = int(input())

print(r.twoSum(nums, target))