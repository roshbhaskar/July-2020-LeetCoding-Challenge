'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n= len(inorder)
        if(n==0): return
        def build(i1,i2,p1,p2):
            if(i1>=i2 or p1>=p2):
                return 
            root = TreeNode(postorder[p2-1])
            ind = inorder.index(postorder[p2-1])
            dif = ind - i1
            root.left = build(i1,i1+dif,p1,p1+dif)
            root.right = build(i1+dif+1,i2,p1+dif,p2-1)
            return root
        return build(0,n,0,n)
        
