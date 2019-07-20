# Filling Bookcase Shelves
# Medium

import math
class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        if shelf_width <= 0:
            raise Exception(" Invalid input")
        if len(books) == 0:
            return 0
        return self.minHeightShelvesCore(books, shelf_width, shelf_width, 0)

    def minHeightShelvesCore(self, books, shelf_width, cur_width, cur_max_height):
        if len(books) == 1:
            if books[0][0] > shelf_width - cur_width:
                return books[0][1] + cur_max_height
            else:
                return max(books[0][1], cur_max_height)

        if books[0][0] > shelf_width - cur_width:
            return self.minHeightShelvesCore(books[1:], shelf_width, books[0][0], books[0][1]) + cur_max_height
        else:
            return min(self.minHeightShelvesCore(books[1:], shelf_width,
                                                 books[0][0], books[0][1]) + cur_max_height,
                       self.minHeightShelvesCore(books[1:], shelf_width,
                                                 books[0][0] + cur_width, max(books[0][1], cur_max_height))
                       )
