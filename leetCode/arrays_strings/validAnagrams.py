"""
    Question:
    242. Valid Anagram
        
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

        Example 1:

        Input: s = "anagram", t = "nagaram"
        Output: true

        Example 2:

        Input: s = "rat", t = "car"
        Output: false
"""


from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Solution 1 - Similar to solution 3 but an inbuilt function to do it
        # return Counter(s) == Counter(t)
    
        #Solution 2 - T(n) = O(nlogn)
        # return sorted(S) == sorted(t)

        #Solution 3
        #Check if length is equal or not
        if(len(s)!=len(t)):
            return False

        #create hashmap    
        letter_count = {}
        for i in s:
            letter_count[i] = letter_count.get(i,0) + 1

        for j in t:
            letter_count[j] = letter_count.get(j, 0) - 1
            if(letter_count[j]<0):
                return False
        
        return True
    


solution = Solution()

print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "cat"))


"""
    Time-complexity = O(n)
    Space-complexity = O(n)
"""