'''
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        result,current=[],[root]
        while current!=[]:
            level,val=[],[]
            for node in current:
                val.append(node.val)
                if(node.left):
                    level.append(node.left)
                if(node.right):
                    level.append(node.right)
            current=level
            result.append(val)
        return result[::-1]
        
