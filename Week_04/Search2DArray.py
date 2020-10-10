class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 方法一：
        # 从左上角开始搜索
        # 复杂度为O(m+n)
        if matrix == []:
            return False
        else:
            rows, columns = len(matrix), len(matrix[0])
            row, column = 0, columns - 1
            while 0 <= row < rows and 0 <= column <= columns:
                if matrix[row][column] == target:
                    return True
                elif matrix[row][column] > target:
                    column -= 1
                else:
                    row += 1
            return False
        # 方法二：
        # 采用二分查找法
        # 时间复杂度O(logn+logm)
        # 方法二：二分查找

        # 获取target所在的行
        def getTargetRow(two_2_arr, target):
            top, bottom = 0, len(matrix) - 1
            temp_column = len(matrix[0]) - 1
            while top < bottom:
                mid = top + (bottom - top) // 2
                if matrix[mid][temp_column] < target:
                    top = mid + 1
                else:
                    bottom = mid
            return top

        # 在target所在的行套用二分搜索方法

        def boolGetTarget(temp_list, target):
            left, right = 0, len(temp_list) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if temp_list[mid] == target:
                    return True
                elif temp_list[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        if matrix == []:
            return False
        else:
            target_row = getTargetRow(matrix, target)
            return boolGetTarget(matrix[target_row], target)
