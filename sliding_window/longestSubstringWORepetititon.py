"""
Question:
    3. Longest Substring without Repetition
    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    
    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        r = 0
        result = 0

        while(r < len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            result = max(result, r - l + 1)
            r += 1
        return result

solution = Solution()

print(solution.lengthOfLongestSubstring("pwwkeaw"))
"""
    Time-complexity = O(n)
    Space-complexity = O(1)

    Alternative solutions:
"""