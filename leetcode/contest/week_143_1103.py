# Distribute candies to people
# Easy

class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        if num_people <= 0 or candies < 0:
            raise Exception("Invalid input")
        result = []
        for i in range(num_people):
            result.append(0)
        if candies == 0:
            return result

        rd, last_candy = self.getRound(candies, num_people)
        for i in range(num_people):
            result[i] += (i+1) * (rd -1)
        index = 0
        while last_candy > (index + 1) * rd:
            result[index] += (index + 1) * rd
            last_candy -= (index + 1) * rd
            index += 1
        result[index] += last_candy
        return result


    def getRound(self, candies, num_people):
        rd = 0
        cur_candy_add = num_people * (1 + num_people) / 2
        cur_candy_sum = 0
        while cur_candy_sum < candies:
            cur_candy_sum += cur_candy_add
            cur_candy_add += num_people * num_people
            rd += 1
        last_candy = candies - (cur_candy_sum - cur_candy_add + num_people * num_people)
        return rd, int(last_candy)


