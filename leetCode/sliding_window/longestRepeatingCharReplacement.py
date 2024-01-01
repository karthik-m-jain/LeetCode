"""
Question:

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