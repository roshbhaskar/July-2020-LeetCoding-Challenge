'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if(root==None):
            return []
        res=[root]
        c=0
        fin=[]
        while(res!=[]):
            result=[]
            x=res
            for i in res:
                if(i):
                    result.append(i.val)
            fin.append(result)
            #result=[]
            res=[]
            if(c%2==0):
                x.reverse()
                for i in x:
                    if(i.right):
                        res.append(i.right)
                    if(i.left):
                        res.append(i.left)
                    
            if(c%2!=0):
                x.reverse()
                for i in x:
                    if(i.left):
                        res.append(i.left)
                    if(i.right):
                        res.append(i.right)
            c+=1
        return fin
                
            
        
