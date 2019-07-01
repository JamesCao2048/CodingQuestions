# Filling Bookcase Shelves
# Medium


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
        heights = [0 for e in range(len(books))]
        book_widths = [book[0] for book in books]
        book_heights = [book[1] for book in books]
        heights[0] = books[0][1]

        for i in range(1, len(books)):
            heights[i] = heights[i - 1] + books[i][1]
            for j in range(0, i):
                print(i, j, sum(book_widths[j:i + 1]))
                if sum(book_widths[j:i + 1]) <= shelf_width:
                    if j > 1:
                        heights[i] = min(heights[i], heights[j - 1] + max(book_heights[j:i + 1]))
                    else:
                        heights[i] = min(heights[i], max(book_heights[j:i + 1]))
                print(heights)
        return heights[len(books) - 1]
