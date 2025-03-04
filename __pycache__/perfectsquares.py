#Given an integer n, return the least number of perfect square numbers that sum to n.
#A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
import math 
def squares(N):
        sqrtN = math.sqrt(N)
        if int(sqrtN) == sqrtN:
            return 1
        
        for i in range(1, int(sqrtN) + 1):
            sqrtN_mii = math.sqrt(N - i*i)
            if int(sqrtN_mii) == sqrtN_mii:
                return 2
        
        while N % 4 == 0:
            N >>= 2
        if N % 8 == 7:
            return 4
        return 3
print(squares(12390230932))