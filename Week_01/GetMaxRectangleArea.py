from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0
        # 方法一：暴力解法
        for i in range(size - 1):
            left = i
            cur_height = heights[i]
            while left > 0 and heights[left - 1] >= cur_height:
                left -= 1

            right = i
            while right < size - 1 and heights[right + 1] >= cur_height:
                right += 1

            max_width = right - left + 1
            res = max(res, max_width * cur_height)
        return res
        # 方法二：采用单调递增栈
        size = len(heights)
        res = 0
        heights = [0] + heights + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        stack = [0]
        size += 2

        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res
