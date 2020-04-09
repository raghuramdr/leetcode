class Solution:
      def twoSum(self, nums, target):
          for idx, num_1 in enumerate(nums):
              for index, num2 in enumerate(nums):
                  if idx == index:
                     continue
                  if num_1+num_2 == target:
                     return [idx, index]
