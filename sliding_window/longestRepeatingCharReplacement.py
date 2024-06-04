"""
Question:
    424. Longest Repeating Character Replacement
    You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
    Return the length of the longest substring containing the same letter you can get after performing the above operations.

    Example 1:

    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

    Example 2:

    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
    There may exists other ways to achieve this answer too.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_hash = {}
        l, r = 0, 0
        res = 0
        max_f = 0

        #Solution 1
        # while (r < len(s)):
        #     char_hash[s[r]] = char_hash.get(s[r], 0) + 1
        #     while ((r - l + 1) - max(char_hash.values())) > k:
        #         char_hash[s[l]] = char_hash.get(s[l]) - 1
        #         l += 1
        #     res = max(res, r-l+1)
        #     r += 1

        #Solution 2
        while (r < len(s)):
            char_hash[s[r]] = char_hash.get(s[r], 0) + 1
            max_f = max(max_f, char_hash[s[r]])
            while ((r - l + 1) - max_f) > k:
                char_hash[s[l]] = char_hash.get(s[l]) - 1
                l += 1
            res = max(res, r-l+1)
            r += 1

        return res
    
solution = Solution()

print(solution.characterReplacement("AABABBA", 1))

"""
    Time-complexity = O(n)
    Space-complexity = O(n)

    Alternative solutions:
    1. Use a hashmap of 26 capital alphabets that you always check and update as you move the window = O(26*n)
"""