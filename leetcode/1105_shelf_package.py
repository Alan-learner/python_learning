class Solution:
    def minHeightShelves(self, books: list, shelfWidth: int) -> int:
        total_height = 0
        books.sort(key=lambda x: x[1])
        total_thickess = sum([k[0] for k in books])
        while total_thickess > shelfWidth and books:
            info = books.pop(-1)
            thickness, height = info
            total_height += height
            remin_thickess = shelfWidth - thickness
            index = -1
            while remin_thickess != 0 and index >= - len(books):
                info = books[index]
                thickness, height = info
                if thickness <= remin_thickess:
                    remin_thickess -= thickness
                    books.pop(index)
                else:
                    index -= 1
            total_thickess = sum([k[0] for k in books])
        if books:
            remin_height = max([k[1] for k in books])
            total_height += remin_height
        print(total_height)
        return total_height


if __name__ == '__main__':
    books = [[9, 9], [5, 4], [3, 1], [1, 5], [7, 3]]
    shelf_width = 10
    s = Solution()
    s.minHeightShelves(books, shelf_width)
