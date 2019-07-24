'''
给定一个有序数组a = [3,7,8,9]，一个二维数组querys = [[2,5], [3,7], [2, 8]], 要求返回对于query中每一项的range，数组在这个范围内的数字个数。
解法一：遍历数组，依次判断数组是否在querys的每个queray的range中并计数，时间复杂度O(n*m)。
解法二：遍历querys，对每个query的start和end在数组中进行二分查找，得到对应位置后再相减。

总结：需要注意边界条件的检查，包括
    1. 二分查找的停止条件，是否可能存在死循环。计算middle是否可能溢出(python中不用考虑)。
    2. 当整个数组都小于或大于target时，是否需要特殊处理。
'''

def binarySearch(a, target):
    lo = 0
    hi = len(a)
    while lo < hi:
        middle = (lo + hi) // 2
        if target == a[middle]:
            return middle
        elif target < a[middle]:
            hi = middle - 1
        else:
            lo = middle + 1
    if a[lo] < target:
        return lo + 1
    return lo

def queryCount(a, querys):
    if len(a) == 0 or len(querys) == 0:
        return None
    result = []
    for query in querys:
        if a[0] > query[1] or a[-1] < query[0]:
            result.append(0)
        else:
            start = binarySearch(a, query[0])
            end = binarySearch(a, query[1])
            result.append(end - start + 1)
    return result