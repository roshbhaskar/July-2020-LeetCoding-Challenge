'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # since each land has 4 sides and if 2 lands are adjacent then their perimeter is decreases by 2
        land = 0
        edge = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]):
                    land += 1
                    if (i > 0 and grid[i-1][j]):
                        edge += 1
                    if (j > 0 and grid[i][j-1]):
                        edge += 1
        return land * 4 - edge * 2
                
              
    
        
        
