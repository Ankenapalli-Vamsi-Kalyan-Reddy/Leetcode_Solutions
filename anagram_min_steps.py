'''
1347. Minimum Number of Steps to Make Two Strings Anagram


You are given two strings of the same length s and t.

In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.

'''


#Steps I followed to solve.

#Initialize a variable count to 0 to keep track of the number of steps needed.
#Iterate through each character i in the string s.
#For each character i, check if it exists in the string t.
#If the character i is found in t, replace the first occurrence of i in t with a placeholder character '@' (to mark it as used).
#If the character i is not found in t, increment the count variable by 1.
#Repeat steps 2-5 until all characters in s have been processed.
#Return the value of count, which represents the minimum number of steps needed to make t an anagram of s.



class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        for i in s:
            if i in t:
                t = t.replace(i, '@', 1)
            else:
                count += 1
        return(count)
