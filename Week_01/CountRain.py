"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，
下雨之后能接多少雨水。
"""


class Solution:

    def trap(self, height: List[int]) -> int:
        # 方法三：双指针的方法
        # 时间复杂度O(n)
        # 空间复杂度O(1)
        

        # 方法二：优化柱子查询方法
        # 时间复杂度O(n)
        # 空间复杂度O(n)
        sum_rain = 0
        max_left_bar_list = [0 for i in range(len(height))]
        max_right_bar_list = [0 for i in range(len(height))]
        for i in range(1, len(height) - 1):
            max_left_bar_list[i] = max(max_left_bar_list[i - 1], height[i - 1])
        for i in range(len(height) - 1, -1, -1):
            max_right_bar_list[i] = max(
                max_right_bar_list[i + 1], height[i + 1])
        for i in range(1, len(height) - 1):
            min_bar = min(max_right_bar_list[i], max_left_bar_list)
            if min_bar > height[i]:
                sum_rain += (min_bar - height[i])
        return sum_rain

        # 方法一：暴利解法如下
        # 时间复杂度O(n*2)
        # 空间复杂度O(1)
        sum_rain = 0
        # 两端的柱子不用考虑，因为没有水可接
        for i in range(1, len(height) - 1):
            # 寻找左边最高的柱子
            max_left_bar = 0
            for j in range(i - 1, -1, -1):
                if height[j] > max_left_bar:
                    max_left_bar = height[j]
            # 寻找右边最高的柱子
            max_right_bar = 0
            for j in range(i + 1, len(height)):
                if height[j] > max_right_bar:
                    max_right_bar = height[j]
            # 取最小的bar
            min_bar = min(max_left_bar, max_right_bar)
            if min_bar > height[i]:
                sum_rain = sum_rain + (min_bar - height[i])
        return sum_rain
