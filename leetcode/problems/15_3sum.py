class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        # print(nums)
        result_list = set()
        for i, num in enumerate(nums):
            if i < len(nums) - 2:
                two_sum_list = self.orderedTwoSum(nums[i + 1:], -num)
                # print(two_sum_list)
                if two_sum_list:
                    for e in two_sum_list:
                        e.append(nums[i])
                        result_list.add(tuple(e))
        # return self.removeRepeatList(result_list)
        return [*map(list, result_list)]

#使用set和不使用set，进行排序的方法速度差不多。开销可能出在函数调用上？

    def orderedTwoSum(self, nums, target):
        i = 0
        j = len(nums) - 1
        result_list = []
        while i < len(nums) and j >= 0 and i < j:
            # print(i, j)
            if nums[i] + nums[j] == target:
                result_list.append([nums[i], nums[j]])
                i += 1
                j -= 1
                while i < len(nums) and nums[i - 1] == nums[i]:
                    i += 1
                while j >= 0 and nums[j + 1] == nums[j]:
                    j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
        return result_list

    def removeRepeatList(self, sum_list):
        [e.sort() for e in sum_list]
        sum_list.sort()
        pre = []
        result_list = []
        for i, e in enumerate(sum_list):
            if not pre == e:
                result_list.append(e)
                pre = e
        return result_list
