# Longest Substring Without Repeating Characters
# Medium

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Solution based on sliding window，使用map记录元素位置，理论上比直接从字符串中查快，实际却慢。
        if not s:
            return 0
        cur_max = 0
        cur_count = 0
        cur_start = 0
        cur_end = 0
        words_dict = {}
        while cur_end < len(s):
            if not s[cur_end] in words_dict.keys() or words_dict[s[cur_end]] < cur_start:
                words_dict[s[cur_end]] = cur_end
                cur_count += 1
                cur_end += 1
                cur_max = max(cur_count, cur_max)
            else:
                cur_start = words_dict[s[cur_end]] + 1
                words_dict[s[cur_end]] = cur_end
                cur_count = cur_end - cur_start + 1
                cur_end += 1
                cur_max = max(cur_count, cur_max)
            #print(cur_start, cur_end, words_dict, cur_max,cur_count)
        return  cur_max