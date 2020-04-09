#### This is the solution to the first problem on Leetcode
#### Problem: Given an array of integers, return indices of the two numbers such#### that they add up to a specific target. You man assume that each input would#### have exactly one solution, and you may not use the same element twice. 


#### Example: Given nums = [2, 7, 11, 15], target = 9,
#### Because nums[0] + nums[1] = 2 + 7 = 9,
#### return [0, 1].


#### Example: Given nums = [3,6,3], target = 6,
#### Because nums[0]+nums[1] = 6, 
#### return [0,2].


#### Example: Given nums = [2,4,6], target = 6,
#### Because nums[0]+nums[1] = 6,
#### return [0,1]


#### problem1.py gives the fastest solution in terms of runtime
#### problem1_1.py is still O(n), but with O(n) memory as well.
#### problem1_2.py is the brute force approach. It is O(n^2) in runtime.
