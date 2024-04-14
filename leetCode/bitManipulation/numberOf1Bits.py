"""
Question: 191. Number of 1 Bits

    Write a function that takes the binary representation of a positive integer and returns the number of 
    set bits
    it has (also known as the Hamming weight).

    Example 1:
    Input: n = 11
    Output: 3
    Explanation: The input binary string 1011 has a total of three set bits.

    Example 2:
    Input: n = 128
    Output: 1
    Explanation: The input binary string 10000000 has a total of one set bit.

    Example 3:
    Input: n = 2147483645
    Output: 30
    Explanation: The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

    Constraints: 1 <= n <= 231 - 1

    Follow up: If this function is called many times, how would you optimize it?
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            # # Solution 1 = (O(no of ones))
            # n = n & (n-1)
            # res += 1

            # # Solution 2 = (O(32))
            # res += n % 2
            # n = n >> 1

            # Solution 3
            res += n % 2
            n = n // 2
        
        return res
        
solution = Solution()
print(solution.hammingWeight(11))

"""
    Time-complexity = O(1)
    Space-complexity = 

    Alternative solutions:
"""