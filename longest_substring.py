# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        self.s = s
        if self.s == '':
            return 0
        length_substring = 1
        string = ''
        for i in range(len(self.s)):
            temp_list = [];temp_list.append(self.s[i]);temp_string = self.s[i];temp_length = 1
            for j in range(i+1,len(self.s)):
                if s[j] in temp_list:
                    temp_list = []
                    if temp_length > length_substring:
                        length_substring = temp_length
                        string = temp_string
                    break
                if s[j] not in temp_list:
                    temp_list.append(self.s[j])
                    temp_length+=1
                    temp_string+=self.s[j]
            if temp_length > length_substring:
                length_substring = temp_length
                string = temp_string
        
        return length_substring




solution = Solution()
s = solution.lengthOfLongestSubstring('au')
print(s)


