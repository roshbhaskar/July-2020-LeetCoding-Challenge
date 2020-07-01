class Solution:
    def arrangeCoins(self, n: int) -> int:
        a = n*2
        return int(math.sqrt(a + 0.25) - 0.5)
    
            
            
                
        