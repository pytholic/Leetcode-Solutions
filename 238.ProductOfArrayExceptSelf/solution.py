class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(
            len(nums)
        ):  # using range instead of enumerate to reverse for postfix
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(
            len(nums) - 1, -1, -1
        ):  # -1 because range does not count last value
            res[i] *= postfix  # directly multiply by already existing value
            postfix *= nums[i]
        return res


solution = Solution()
nums = [1, 2, 3, 4]
res = solution.productExceptSelf(nums)
print(res)
