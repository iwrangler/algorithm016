class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        # 二分法
        left, right = 1, num
        while left <= right:
            mid = (left + round((right - left) / 2))
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
        # 牛顿迭代法
        # if num < 2:
        #     return True

        # x = num // 2
        # while x * x > num:
        #     x = (x + num // x) // 2
        # return x * x == num
