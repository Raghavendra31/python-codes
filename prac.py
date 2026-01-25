# nums = list(map(int, input().split()))
# target = int(input())
# print(nums)
# for num in range(len(nums)):
#     if (num + 1) in range(len(nums)):
#         for n in range(len(nums)):
#             if (n+1) in range(len(nums)):
#                 output = nums[num] + nums[n+1]
#                 if output is target:
#                     print(f"[{num},{n+1}]")


# nums = [2,7,11,15]
# target = 9

# for num in range(len(nums)):
#     if (num + 1) in range(len(nums)):
#         for n in range(len(nums)):
#             if (n+1) in range(len(nums)):
#                 output = nums[num] + nums[n+1]
#                 if output is target:
#                     print(f"[{num},{n+1}]")


class Solution():
    def addTwoNumbers(self, l1, l2):
        l1.reverse()
        l2.reverse()
        #how to sum list elements
        l1 = int(''.join(map(str, l1)))
        l2 = int(''.join(map(str, l2)))
        output = l1 + l2
        #split the output and place it in the list
        output = [int(x) for x in str(output)]
        output.reverse()
        return output
    

s = Solution()
print(s.addTwoNumbers([2,4,3], [5,6,4]))


# 