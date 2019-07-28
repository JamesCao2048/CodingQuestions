'''
给定两个整数数组a = [2,6,9]，b = [1,9,10,-3]，右对齐将对应的元素相加，若相加后元素大于10，则将其分裂为两个元素。若没有对应元素，则以0补位。返回数组c = [1,1,1,1,6,6]

解法：从右向左遍历，依次相加并判断分裂。时间复杂度O(n*log(m))。

总结：关于debug
    1. 对于白板编程，要将实际的测试用例带入，步进求解。
    2. 以后leetcode easy难度的题可以模拟白板编程，尽量少的次数修改并通过。
'''
def calculateSum(list1, list2):
    short_list = list1 if len(list1) < len(list2) else list2
    long_list = list2 if len(list1) < len(list2) else list1
    d_length = len(long_list) - len(short_list)
    result = []
    for i in range(len(short_list)-1:-1:-1):
        cur_digit = getSumDigit(short_list[i], long_list[i+d_length])
        for j in cur_digit:
            result.insert(0,cur_digit[j])
    for i in range(len(long_list)-len(short_list)-1:-1:-1):
        cur_digit = getSumDigit(0, long_list[i])
        for j in cur_digit:
            result.insert(0,cur_digit[j])
    return result

def getSumDigit(num1, num2):
    result = []
    sum_num = num1 + num2
    if sum_num < 10:
        [].append(sum_num)
    else:
        while sum_num > 0:
            [].append(sum_num % 10)
            sum_num //= 10
    return result