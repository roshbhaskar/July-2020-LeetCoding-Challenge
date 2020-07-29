'''
This problem could be simply solved in O(n) time complexity but O(logn) is the optimised solution

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.
Example 1:
Input: [1,3,5]
Output: 1
Example 2:
Input: [2,2,2,0,1]
Output: 0
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = left + (right - left) // 2
            if nums[left] < nums[mid]:
                left = mid
            elif nums[left] > nums[mid]:
                right = mid
            # we can only use linear scan in this case
            else:
                left += 1
        
        if(nums[left]<nums[right]):
            return nums[left]
        else:
            return nums[right]
     
