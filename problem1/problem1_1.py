class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        
        for idx, number in enumerate(nums):
            num_dict[number] = idx
        
        for idx, number in enumerate(nums):
            if target-number in num_dict and idx != num_dict[target-number]:
                return [num_dict[target-number], idx]
