"""
Question:
    567. Permutation in String
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
    In other words, return true if one of s1's permutations is the substring of s2.

    Example 1:

    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").

    Example 2:

    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false

    Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #Solution 1
        # s1hash, s2hash = [0] * 26, [0] * 26
        # l, r = 0, 0

        # if (len(s1) > len(s2)):
        #     return False

        # for i in range(len(s1)):
        #     index = ord(s1[i]) - ord('a')
        #     s1hash[index] += 1

        # for r in range(len(s2)):
        #     s2hash[ord(s2[r]) - ord('a')] += 1
        #     if (r-l+1) == len(s1):
        #         matches = 0
        #         for i in range(0, 27):
        #             if matches == 26:
        #                 return True
        #             elif s1hash[i] != s2hash[i]:
        #                 s2hash[ord(s2[l]) - ord('a')] -= 1
        #                 l += 1
        #                 break
        #             else:
        #                 matches += 1 
        # return False

        #Solution 2
        s1hash, s2hash = [0] * 26, [0] * 26
        l = 0
        matches = 0

        if (len(s1) > len(s2)):
            return False

        for i in range(len(s1)):
            index1 = ord(s1[i]) - ord('a')
            index2 = ord(s2[i]) - ord('a')
            s1hash[index1] += 1
            s2hash[index2] += 1

        for i in range(26):
            if s1hash[i] == s2hash[i]:
                matches += 1
            else:
                matches += 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2hash[index] += 1

            if s2hash[index] -1 == s1hash[index]:
                matches -= 1
            elif s2hash[index] == s1hash[index]:
                matches += 1

            l_index = ord(s2[l]) - ord('a')
            s2hash[l_index] -= 1
        
            if s2hash[l_index] == s1hash[l_index]:
                matches += 1
            elif s2hash[l_index]+1 == s1hash[l_index]:
                matches -= 1
            l += 1

        return matches == 26
    
solution = Solution()

print(solution.checkInclusion("ab", "eidbaooo"))

"""
    Solution 1:
    Time-complexity = O(26n)
    Space-complexity = O(1)

    Solution 2:
    Time-complexity = O(n)
    Space-complexity = O(1)
"""


