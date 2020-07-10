'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  
1 is typically treated as an ugly number.
n does not exceed 1690.

'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly=[0]*n
        ugly[0]=1
        i2=i3=i5=0
        next_2=2
        next_3=3
        next_5=5
        for i in range(1,n):
            ugly[i]=min(next_2,next_3,next_5)
            if(ugly[i]==next_2):
                i2=i2+1
                next_2=ugly[i2]*2
            if(ugly[i]==next_3):
                i3+=1
                next_3=ugly[i3]*3
            if(ugly[i]==next_5):
                i5+=1
                next_5=ugly[i5]*5
        return ugly[-1]
            
                
        
