# [LC] 74 - Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix, target):
        # top right corner에서 시작해서,
        # 보고있는 값 < target 이면, target은 해당 row에 존재할 수 없음 => row 늘려나가기
        # 보고있는 값 > target 이면, target은 해당 col에 존재할 수 없음 => col 늘려나가기
        r, c = 0, len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
            else:
                return True
        return False

class Solution2:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col - 1

        while l < r:
            mid = (l + r) // 2
            if matrix[mid // col][mid % col] < target:
                l = mid + 1
            else:
                r = mid
            # elif matrix[mid // col][mid % col] > target:
            #     r = mid + 1
            # else:
            #     return True

        return matrix[l // col][l % col] == target
        # return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
sol = Solution()
sol2 = Solution2()
print(sol.searchMatrix(matrix, target))
print(sol2.searchMatrix(matrix, target))
