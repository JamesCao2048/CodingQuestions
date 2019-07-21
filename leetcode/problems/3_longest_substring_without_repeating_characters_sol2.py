# Longest Substring Without Repeating Characters
# Medium

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # DP Solution based on record_start. str.index比str.find快很多
        if not s:
            return 0
        counts = [0] * len(s)
        counts[0] = 1
        cur_start = 0
        for i in range(1, len(s)):
            if not s[i] in s[cur_start:i]:
                counts[i] = counts[i-1] + 1
            else:
                cur_start = s[cur_start: i].index(s[i]) + 1 + cur_start
                counts[i] = i - cur_start + 1
            print(i, cur_start, counts[i])
        return max(counts)