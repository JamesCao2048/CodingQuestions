# Longest Substring Without Repeating Characters
# Medium

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # DP Solution based on map, not satisfactory.
        if not s:
            return 0
        word_set = {}
        counts = [0] * len(s)
        word_set[s[0]] = 0
        counts[0] = 1
        for i in range(1, len(s)):
            if not s[i] in word_set.keys():
                counts[i] = counts[i-1] + 1
                word_set[s[i]] = i
            else:
                for key,value in word_set.items():
                    if value < word_set[s[i]]:
                        word_set.pop(key)
                counts[i] = i - word_set[s[i]]
                word_set[s[i]] = i
        return max(counts)


