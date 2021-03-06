'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp_result = [] # this will store values [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]] after calling sub function
        self.sub(nums,[0 for i in range(len(nums))],temp_result,0)
        main_result = []
        for lists in temp_result:
            temp = []
            for i in range(len(lists)):
                if lists[i] == 1:
                    temp.append(nums[i])
            main_result.append(temp)
        return temp_result
    def sub(self,nums,temp,result,index):
        if index == len(nums):
            result.append([i for i in temp])
            #print(temp)
            return
        temp[index] = 0
        self.sub(nums,temp,result,index+1)
        temp[index] = 1
        self.sub(nums, temp, result,index + 1) 
                
                
                
        
        
