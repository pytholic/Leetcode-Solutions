"""
You must write an algorithm that runs in O(n) time 
and without using the division operation.
"""

# O(n^2)
# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         res = []
#         for val in nums:
#             product = 1
#             for i in range(len(nums)):
#                 if nums[i] != val:
#                     product *= nums[i]
#             res.append(product)
#         return res


# solution = Solution()
# nums = [1, 2, 3, 4]
# res = solution.productExceptSelf(nums)
# print(res)


# import math
# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         res = []
#         for i in range(len(nums)):
#             # tmp = nums[0]
#             # nums.remove(nums[0])
#             tmp = nums.pop(0)
#             prod = math.prod(nums)
#             nums.append(tmp)
#             res.append(prod)
#         return res


# solution = Solution()
# nums = [1, 2, 3, 4]
# res = solution.productExceptSelf(nums)
# print(res)

# This solution gave me time exceed error on leet code

# """
# All values before index -> multipy
# All values after
# Then total product
# """

# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         res = []
#         for idx in range(len(nums)):
#             pre = nums[:idx]
#             post = nums[idx + 1 :]
#             pre_prod = math.prod(pre)
#             post_prod = math.prod(post)
#             prod = pre_prod * post_prod
#             res.append(prod)
#         return res


# solution = Solution()
# nums = [1, 2, 3, 4]
# res = solution.productExceptSelf(nums)
# print(res)

#
