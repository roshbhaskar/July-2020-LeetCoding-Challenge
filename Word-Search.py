'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

'''

class Solution:
    def dfs(self,board,word,i,j,k):
        if(k==len(word)):
            return True
        if(i<0 or j<0 or j>=len(board[0]) or i>=len(board) or word[k]!=board[i][j]):
            return False
        temp = board[i][j]
        board[i][j]='#'
        found = self.dfs(board,word,i+1,j,k+1) or self.dfs(board,word,i-1,j,k+1) or self.dfs(board,word,i,j+1,k+1) or self.dfs(board,word,i,j-1,k+1)
        board[i][j] = temp
        return found
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        for  i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]== word[0] and self.dfs(board,word,i,j,0)):
                    result = True
        return result
  
