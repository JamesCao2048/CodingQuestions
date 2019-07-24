# ZigZag Conversion
# Medium

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 根据每行索引增加规律计算
        if len(s) <= numRows or numRows < 2:
            return s
        result = ""
        for i in range(numRows):
            round = 1
            result += s[i]
            index = i
            while index < len(s):
                if round:
                    offset = (numRows - i -1) * 2
                else:
                    offset = i * 2
                round = 1 - round
                index += offset
                if index < len(s) and offset:
                    result += s[index]
            #print(result)
                
        return result
