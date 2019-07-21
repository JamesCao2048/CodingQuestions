# Longest Substring Without Repeating Characters
# Hard
# Not completed

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 先找到nums1的中位数在nums2中的位置，之后再二分查找比较判断元素(顺序不行)。
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 == 0 and len2 == 0:
            return None

        m1_value = self.medianOfArray(nums1)
        m2_value = self.medianOfArray(nums2)
        if len1 == 0:
            return m2_value
        if len2 == 0:
            return m1_value

        m1_nums2_position = self.binarySearch(m1_value, nums2)
        if m1_nums2_position + len1//2 == (len1 + len2)//2:
            return m1_value
        index1 = len1//2
        index2 = m1_nums2_position
        if m1_nums2_position + len1//2 < (len1 + len2)//2:
            count = (len1 + len2)//2 - m1_nums2_position + len1//2
            while not count == 0:
                if index1 + 1 < len1 and nums1[index1+1] < nums2[index2]:
                    index1 += 1
                    count -= 1
                else:
                    index2 += 1
                    count -=1
        else:
            count = m1_nums2_position + len1 // 2 - (len1 + len2) // 2
            while not count == 0:
                if index1 - 1 >= 0 and nums1[index1 - 1] > nums2[index2]:
                    index1 -= 1
                    count -= 1
                else:
                    index2 -= 1
                    count -= 1

    def binarySearch(self, target, nums):
        lo = 0
        hi = len(nums)
        middle = (lo + hi) // 2
        while lo < hi:
            if target == nums[middle]:
                return middle
            if target < nums[middle]:
                hi = middle
                middle = (lo + hi) // 2
            else:
                lo = middle + 1
                middle = (lo + hi) // 2
        return lo

    def medianOfArray(self, nums):
        l = len(nums)
        if l % 2:
            return nums[l // 2]
        else:
            return (nums[l // 2] + nums[l // 2 - 1]) /2


