"""
旋转数组中只存在三种情况：
左<中<右：去左侧区间 [1 2 3 4 5 6 7]
右<左<中：去右侧区间 [6 7 8 9 1 2 3]
中<右<左：去左侧区间 [6 7 8 1 3 4 5]

"""
# 时间复杂度 O(logN)
# 空间复杂度 O(1)


class Solution:

    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                # 之所以不是mid+1 是因为mid有可能为最小值
                high = mid
            else:
                low = mid + 1
        return nums[low]
