'''
Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        a = n*2
        return int(math.sqrt(a + 0.25) - 0.5)
    
            
            
                
        
