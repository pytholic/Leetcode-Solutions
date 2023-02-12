class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target

        diff = {}

        for idx1, num1 in enumerate(nums):
            num2 = target-num1
            if num2 in diff.keys():
                idx2 = diff[num2]
                return[idx1, idx2]
            else:
                diff[num1] = idx1
                
        return None