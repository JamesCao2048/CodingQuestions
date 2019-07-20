# Statistics from a Large Sample
# Medium

from decimal import *
import math
class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        #getcontext().prec = 8
        min_number = -1
        max_number = -1
        mode_number = [-1, 0]

        #number_sum = Decimal(0)
        #浮点数的精度够了，不需要用开销比较大的Decimal
        number_sum = 0.0
        number_num = 0
        median_number = 0

        for i, n in enumerate(count):
            if n:
                if min_number < 0:
                    min_number = i
                max_number = max(max_number, i)
                if mode_number[1] < n:
                    mode_number[0] = i
                    mode_number[1] = n
                number_sum += i * n
                number_num += n
        assert number_num > 0, "count all zeros"

        median_index = int(math.floor(number_num / 2) + 1)
        print(number_num, median_index)
        cur_count = 0
        pre_index = -1
        for i, n in enumerate(count):
            cur_count += n
            if cur_count >= median_index:
                # print(cur_count, n, median_index -1, i)
                if number_num % 2:
                    median_number = i
                elif cur_count - n < median_index - 1:
                    median_number = i
                else:
                    median_number = (i + pre_index) / 2
                break
            if n:
                pre_index = i
        mean_number = number_sum / number_num
        return [min_number, max_number, float(str(mean_number)), median_number, mode_number[0]]
