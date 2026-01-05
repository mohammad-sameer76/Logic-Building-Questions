class Solution:
    def sumOfSquares(self, number):
        Sum=0
        for i in range(1,number+1):
            Sum+=i**2
        return Sum